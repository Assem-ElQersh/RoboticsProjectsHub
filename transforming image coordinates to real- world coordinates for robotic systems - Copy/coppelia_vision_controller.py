import math
import time

import cv2
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient


class CoppeliaVisionController:
    def __init__(self):
        self.client = RemoteAPIClient()
        self.sim = self.client.require('sim')
        self.robot_handle = None
        self.target_handle = None
        self.vision_sensor = None
        self.camera_matrix = None
        self.resolution = None
        self.ik_target_handle = None
        self.joints = []
        
    def setup_scene(self):
        """Setup the scene with vision sensor and robot"""
        print("Loading scene...")
        
        # Get robot handle and setup IK
        try:
            self.robot_handle = self.sim.getObject('./redundantRobot')
            print("Robot found successfully")
        
            # Get manipSphere and target
            try:
                self.manip_sphere = self.sim.getObject('./redundantRobot/manipSphere')
                self.redundant_target = self.sim.getObject('./redundantRobot/manipSphere/redundantRob_target')
                print("Found manipSphere and target")
            except:
                print("Could not find manipSphere or target")
                raise
            
            # Get all joints
            base_name = "./redundantRobot/joint"
            for i in range(1, 8):  # Assuming 7 joints
                try:
                    joint = self.sim.getObject(f"{base_name}{i}")
                    self.joints.append(joint)
                    print(f"Found joint {i}")
                except:
                    break
            
            if not self.joints:
                raise Exception("No joints found for the robot")
                
            print(f"Found {len(self.joints)} robot joints")
            
            # Set up movement parameters
            vel = 110 * math.pi / 180
            accel = 40 * math.pi / 180
            jerk = 80 * math.pi / 180

            self.maxVel = [vel] * 7  # One for each joint
            self.maxAccel = [accel] * 7
            self.maxJerk = [jerk] * 7
            
            # Get the tip
            try:
                self.tip = self.sim.getObject('./redundantRobot/joint7/link/redundantRob_tip')
                print("Found robot tip")
            except:
                print("Could not find robot tip")
                raise
                
            # Set up vision sensor
            try:
                possible_paths = ['./Vision_sensor', '/Vision_sensor', 'Vision_sensor']
                for path in possible_paths:
                    try:
                        self.vision_sensor = self.sim.getObject(path)
                        if self.vision_sensor is not None:
                            print(f"Vision sensor found at path: {path}")
                            break
                    except:
                        continue
                        
                if self.vision_sensor is None:
                    raise Exception("Vision sensor not found. Please add a Vision Sensor to the scene and name it 'Vision_sensor'")
                    
                self.resolution = self.sim.getVisionSensorResolution(self.vision_sensor)
                print(f"Vision sensor resolution: {self.resolution}")
                
            except Exception as e:
                print(f"Error setting up vision sensor: {str(e)}")
                raise
                
        except Exception as e:
            print(f"Error finding robot: {str(e)}")
            raise

    def create_perspective_matrix(self, fov_degrees, aspect, near, far):
        """Create perspective projection matrix"""
        try:
            fov = math.radians(float(fov_degrees))
            f = 1.0 / math.tan(fov / 2)
            return np.array([
                [f/aspect, 0, 0, 0],
                [0, f, 0, 0],
                [0, 0, (far+near)/(near-far), (2*far*near)/(near-far)],
                [0, 0, -1, 0]
            ], dtype=np.float32)
        except Exception as e:
            print(f"Error in create_perspective_matrix: {str(e)}")
            print(f"Debug info - fov_degrees: {fov_degrees, aspect, near, far}")
            raise

    def get_vision_sensor_data(self):
        """Get image from vision sensor"""
        if self.vision_sensor is None:
            return None
        
        img, resolution = self.sim.getVisionSensorImg(self.vision_sensor)
        if img:
            # Convert the raw image data to numpy array
            img = np.frombuffer(img, dtype=np.uint8).reshape(resolution[1], resolution[0], 3)
            
            # In CoppeliaSim images are left to right (x-axis), and bottom to top (y-axis)
            # We need to flip it for correct orientation in OpenCV
            img = cv2.flip(img, 0)  # Flip vertically
            
            # Convert from RGB to BGR for OpenCV
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            
            return img
        return None

    def pixel_to_world(self, pixel_point):
        """Convert pixel coordinates to world coordinates"""
        if self.vision_sensor is None:
            return (0, 0, 0)
        
        # Get vision sensor pose
        sensor_position = self.sim.getObjectPosition(self.vision_sensor, -1)
        sensor_orientation = self.sim.getObjectOrientation(self.vision_sensor, -1)
        
        # Normalize pixel coordinates to [-1, 1]
        # Flip the x coordinate by subtracting from resolution width
        flipped_x = self.resolution[0] - pixel_point[0]  # Flip X coordinate
        x = (2.0 * flipped_x / self.resolution[0] - 1.0)
        y = (1.0 - 2.0 * pixel_point[1] / self.resolution[1])
        
        # Create ray from camera
        ray_start = sensor_position
        ray_dir = self.get_ray_direction(x, y, sensor_orientation)
        
        # Calculate the target point (assuming a plane at z=0)
        if ray_dir[2] != 0:  # Avoid division by zero
            t = -ray_start[2] / ray_dir[2]  # Parameter for intersection with z=0 plane
            world_point = [
                ray_start[0] + t * ray_dir[0],
                ray_start[1] + t * ray_dir[1],
                0  # We're assuming the workspace is at z=0
            ]
            return world_point
        return ray_start

    def get_ray_direction(self, x, y, sensor_orientation):
        """Calculate ray direction from normalized device coordinates"""
        # Create ray in camera space
        fov = math.pi/4  # 45 degrees field of view
        tan_fov = math.tan(fov/2)
        
        ray_dir = np.array([
            x * tan_fov,
            y * tan_fov,
            -1.0  # Camera looks along negative Z
        ])
        
        # Normalize the ray direction
        ray_dir = ray_dir / np.linalg.norm(ray_dir)
        
        # Create rotation matrix from euler angles
        rotation_matrix = self.euler_to_rotation_matrix(sensor_orientation)
        
        # Apply camera rotation
        ray_dir = rotation_matrix.dot(ray_dir)
        return ray_dir

    def euler_to_rotation_matrix(self, euler):
        """Convert euler angles to rotation matrix"""
        # Roll (X-axis rotation)
        Rx = np.array([
            [1, 0, 0],
            [0, math.cos(euler[0]), -math.sin(euler[0])],
            [0, math.sin(euler[0]), math.cos(euler[0])]
        ])
        
        # Pitch (Y-axis rotation)
        Ry = np.array([
            [math.cos(euler[1]), 0, math.sin(euler[1])],
            [0, 1, 0],
            [-math.sin(euler[1]), 0, math.cos(euler[1])]
        ])
        
        # Yaw (Z-axis rotation)
        Rz = np.array([
            [math.cos(euler[2]), -math.sin(euler[2]), 0],
            [math.sin(euler[2]), math.cos(euler[2]), 0],
            [0, 0, 1]
        ])
        
        # Combined rotation matrix
        return Rz.dot(Ry.dot(Rx))

    def move_robot(self, pixel_point):
        """Move robot to clicked position"""
        try:
            world_point = self.pixel_to_world(pixel_point)
            print(f"Moving to world coordinates: {world_point}")
            
            # Get current target pose
            current_pose = self.sim.getObjectPose(self.redundant_target)
            
            # Create new target pose (keeping orientation, updating position)
            target_pose = current_pose.copy()
            target_pose[0] = world_point[0]  # X position
            target_pose[1] = world_point[1]  # Y position
            target_pose[2] = 0.1  # Z position (slightly above workspace)
            
            # Set up movement parameters
            params = {
                'object': self.redundant_target,
                'targetPose': target_pose,
                'maxVel': [0.5, 0.5, 0.5, 0.5],  # Linear and angular velocities
                'maxAccel': [0.1, 0.1, 0.1, 1.0],  # Linear and angular accelerations
                'maxJerk': [3.0, 3.0, 3.0, 3.0]  # Linear and angular jerks
            }
            
            # Move to position
            self.sim.moveToPose(params)
            
            print(f"Target position set to: {world_point}")
            
        except Exception as e:
            print(f"Error in move_robot: {str(e)}")
            raise

    def start_simulation(self):
        """Start CoppeliaSim simulation"""
        # Make sure simulation is fully stopped first
        self.sim.stopSimulation()
        time.sleep(0.1)
        
        # Start simulation with real-time synchronization
        self.sim.setBoolParameter(self.sim.boolparam_realtime_simulation, True)
        self.sim.setFloatParameter(self.sim.floatparam_simulation_time_step, 0.05)
        self.sim.startSimulation()
        print("Simulation started with realtime sync")

    def stop_simulation(self):
        """Stop CoppeliaSim simulation"""
        self.sim.stopSimulation()
        print("Simulation stopped")