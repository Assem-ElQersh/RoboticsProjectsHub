import cv2
import numpy as np

path = "./red1.png"
original_image = cv2.imread(path)
cv2.imshow("image", original_image)
cv2.waitKey(0)

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv_image", hsv_image)
cv2.waitKey(0)

# Define lower and upper bounds for the red color in HSV
lower_red1 = np.array([0, 75, 20])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([160, 75, 20])
upper_red2 = np.array([180, 255, 255])

# Create masks to detect the red color in both specified ranges
lower_mask = cv2.inRange(hsv_image, lower_red1, upper_red1)
upper_mask = cv2.inRange(hsv_image, lower_red2, upper_red2)
cv2.imshow("lower_mask", lower_mask)
cv2.imshow("upper_mask", upper_mask)


# Combine the lower and upper masks to get a single mask
combined_mask = lower_mask + upper_mask
cv2.imshow("combined_mask", combined_mask)
cv2.waitKey(0)

# Calculate the moments of the combined mask to find the centroid
moments = cv2.moments(combined_mask)

centroid_x = 0
centroid_y = 0
# Check if moments['m00'] is not zero before computing centroid
if moments['m00'] != 0:
    centroid_x = int(moments['m10'] / moments['m00'])
    centroid_y = int(moments['m01'] / moments['m00'])

    print(f"Centroid Y-coordinate is {centroid_y}")
    print(f"Centroid X-coordinate is {centroid_x}")

    # Draw an arrow from the center to the centroid
    cv2.arrowedLine(original_image, (int(original_image.shape[1]/2), int(original_image.shape[0])), (centroid_x, centroid_y), (255, 0, 0), 2, tipLength=0.5)

steering = (centroid_x - (hsv_image.shape[1]/2)) / (hsv_image.shape[1]/2)

# Display the image with the arrow
cv2.imshow("Vector", original_image)


# this part will work on raspberry, when we have the motors functions  

# if steering < - 0.5:
#     right()
# elif steering > 0.5:
#     left()
# else
#     forward()


# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()