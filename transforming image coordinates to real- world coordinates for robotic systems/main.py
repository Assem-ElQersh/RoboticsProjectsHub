from coppelia_vision_controller import CoppeliaVisionController
import cv2

def main():
    # Initialize controller
    controller = CoppeliaVisionController()
    
    # Setup scene
    print("Setting up scene...")
    try:
        controller.setup_scene()
        controller.start_simulation()
        
        # Main control loop
        while True:
            # Get vision sensor image
            img = controller.get_vision_sensor_data()
            if img is None:
                print("Could not get vision sensor data")
                break
                
            # Display image for clicking
            def mouse_callback(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    print(f"Clicked at pixel coordinates: ({x}, {y})")
                    controller.move_robot((x, y))
            
            cv2.namedWindow('CoppeliaSim Vision')
            cv2.setMouseCallback('CoppeliaSim Vision', mouse_callback)
            
            cv2.imshow('CoppeliaSim Vision', img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
                
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if controller:
            controller.stop_simulation()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()