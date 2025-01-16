import numpy as np

L1 = 5
L2 = 4

def line_y(x):
    return -x / 2 + 10

step_size = 0.2
x_values = np.arange(-10, 15, step_size)
points = [(x, line_y(x)) for x in x_values]

def is_reachable(x, y):
    return np.sqrt(x**2 + y**2) <= (L1 + L2)

def inverse_kinematics(x, y):
    d = np.sqrt(x**2 + y**2)
    cos_theta2 = (d**2 - L1**2 - L2**2) / (2 * L1 * L2)
    sin_theta2 = np.sqrt(1 - cos_theta2**2)
    theta2 = np.arctan2(sin_theta2, cos_theta2)
    
    k1 = L1 + L2 * cos_theta2
    k2 = L2 * sin_theta2
    theta1 = np.arctan2(y, x) - np.arctan2(k2, k1)
    
    return theta1, theta2

reachable_points = []
angles = []
for x, y in points:
    if is_reachable(x, y):
        theta1, theta2 = inverse_kinematics(x, y)
        reachable_points.append((x, y))
        angles.append((theta1, theta2))

def compute_line_length(points):
    length = 0
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        length += np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return length

max_length = compute_line_length(reachable_points)

print(f"Maximum trackable length of the line: {max_length:.2f} cm")
print(f"Number of reachable points: {len(reachable_points)}")
