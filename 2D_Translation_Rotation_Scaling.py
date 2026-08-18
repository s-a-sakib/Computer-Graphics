import numpy as np
import matplotlib.pyplot as plt

def translate(points, translation_vector):
    return points + translation_vector

def rotate(points, angle):
    angle_rad = np.radians(angle)
    rotated = []
    
    for x, y in points:
        r = np.sqrt(x**2 + y**2)
        angle1 = np.arctan2(y, x)      # handles all quadrants + x=0
        x_new = r * np.cos(angle1 + angle_rad)
        y_new = r * np.sin(angle1 + angle_rad)
        rotated.append([x_new, y_new])
    
    return rotated

def scale(points, sx, sy):
    return [[x * sx, y * sy] for x, y in points]

# points = np.array([[1, 1],
#     [4, 1],
#     [2.5, 4],
#     [1, 1]])

# translation_vector = np.array([3, 3])
# angle = 60  
# scaling_factors = [2, 3]

# # Apply transformations
# translated_points = translate(points, translation_vector)
# rotated_points = rotate(points, angle)
# scaled_points = scale(points, *scaling_factors)

# print("Original Points:\n", points)
# print("Translated Points:\n", translated_points)
# print("Rotated Points:\n", rotated_points)
# print("Scaled Points:\n", scaled_points)


# # Plotting
# plt.figure(figsize=(10, 10))

# plt.subplot(2, 2, 1)
# plt.title("Translated Points")
# plt.plot(points[:, 0], points[:, 1], 'bo-', label='Original')
# plt.plot(translated_points[:, 0], translated_points[:, 1], 'ro-', label='Translated')
# plt.legend()
# plt.grid()

# plt.subplot(2, 2, 2)
# plt.title("Rotated Points")
# rotated_points = np.array(rotated_points)
# plt.plot(points[:, 0], points[:, 1], 'bo-', label='Original')
# plt.plot(rotated_points[:, 0], rotated_points[:, 1], 'ro-', label='Rotated')
# plt.legend()
# plt.grid()

# plt.subplot(2, 2, 3)
# plt.title("Scaled Points")
# scaled_points = np.array(scaled_points)
# plt.plot(points[:, 0], points[:, 1], 'bo-', label='Original')
# plt.plot(scaled_points[:, 0], scaled_points[:, 1], 'ro-', label='Scaled')
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.show()

