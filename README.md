# RoboticsProjectsHub

A collection of robotics simulation projects focusing on path planning, obstacle avoidance, kinematics, and computer vision integration. This repository contains a variety of robotics applications and algorithms implemented in Python.

## Table of Contents

- [Bug Algorithms](#bug-algorithms)
- [Interactive 2-Link Manipulator](#interactive-2-link-manipulator)
- [Math Function Rotator](#math-function-rotator)
- [Simple Path Planning in a Square Room](#simple-path-planning-in-a-square-room)
- [Image Coordinates to Real-World Coordinates](#image-coordinates-to-real-world-coordinates)
- [Requirements](#requirements)
- [License](#license)

## Bug Algorithms

Implementation of classical Bug algorithms (Bug 0, Bug 1, and Bug 2) for robot path planning with obstacle avoidance.

### Features:
- Bug 0: Greedy algorithm that moves towards the goal until hitting an obstacle, then moves around it until it can resume direct goal-seeking
- Bug 1: Enhanced algorithm that traverses the entire obstacle perimeter to find the closest point to the goal
- Bug 2: Optimized algorithm that follows the M-line (start-to-goal line) when possible

### Usage:
```python
python bug_algorithms/code.py
```
You can specify which bug algorithm to run by modifying the parameters at the end of the script:
```python
if __name__ == '__main__':
    main(bug_0=True, bug_1=False, bug_2=False)
```

## Interactive 2-Link Manipulator

A 2-link robotic arm simulation that tracks a line function in its workspace.

### Features:
- Inverse kinematics to calculate joint angles
- Calculation of workspace reachability
- Animation of the manipulator's movement

### Usage:
For the analysis script:
```python
python interactive_2-link_manipulator/Answer.py
```

For the interactive simulation:
```python
python interactive_2-link_manipulator/Simulation_Animation.py
```

## Math Function Rotator

An interactive visualization tool for rotating mathematical functions.

### Features:
- Interactive slider for rotation angle control
- Toggle between different mathematical functions (sin, cos, tan)
- Real-time visualization of both original and rotated functions

### Usage:
```python
python math_function_rotator/MathFunctionRotator.py
```

## Simple Path Planning in a Square Room

Implementation of Breadth-First Search (BFS) for path planning in a discretized environment.

### Features:
- Grid-based path planning
- Obstacle avoidance
- Animated visualization of path discovery

### Usage:
```python
python simple_path_planning_in_a_square_room/Answer.py
```

## Image Coordinates to Real-World Coordinates

A system for transforming camera image coordinates into real-world coordinates for robotic manipulation, integrated with CoppeliaSim.

### Features:
- Camera-to-world coordinate transformation
- Interactive click-to-move functionality
- Integration with CoppeliaSim's Remote API
- Control of a redundant robotic manipulator

### Requirements:
- CoppeliaSim (formerly V-REP)
- ZMQ Remote API client for CoppeliaSim
- OpenCV

### Usage:
1. Start CoppeliaSim and load the `redundantRobot-python.ttt` scene
2. Run the main script:
```python
python transforming_image_coordinates_to_real_world_coordinates/main.py
```
3. Click on the camera view to command the robot to move to that location

## Requirements

- Python 3.7+
- NumPy
- Matplotlib
- OpenCV (for vision projects)
- Plotly (for interactive visualizations)
- CoppeliaSim (for the robotic manipulation project)
- coppeliasim_zmqremoteapi_client (for CoppeliaSim communication)

Install Python dependencies:
```bash
pip install numpy matplotlib opencv-python plotly
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Assem-ElQersh/RoboticsProjectsHub/blob/main/LICENSE) file for details.
