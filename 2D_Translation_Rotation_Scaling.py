import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def translate(point, traslation_vector):
    return point + traslation_vector

def rotate(points, angle):

    angle = np.radians(angle)

    rotated = []

    for x, y in points:

        r = np.sqrt(x**2 + y**2)
        fi = np.arctan2(y, x)

        x_new = r * np.cos(angle + fi)
        y_new = r * np.sin(angle + fi)

        rotated.append([x_new, y_new])

    return np.array(rotated)

def scale(points, sx, sy):
    return np.array([[x * sx, y * sy] for x, y in points])

points = np.array([
    [1,1], [4,1], [2.5,4], [1,1]
])


translation = np.array([5, 5])
angle = 60
Scale_factor = np.array([3, 4])

fig, ax = plt.subplots(figsize=(8, 8))


def update(frame):

    ax.clear()
    ax.set_xlim(-10,20)
    ax.set_ylim(-10,20)

    ax.grid()
    ax.set_title("2D Transformations")

    # Oridinal Image
    ax.plot(points[:,0], points[:,1], label = "Oridinal")

    # Translation
    translate_point = translate(points, translation * frame / 100)
    ax.plot(translate_point[:,0], translate_point[:,1],  label = "Translated")

    # Rotation
    rotated_point = rotate(points, angle * frame/100)
    ax.plot(rotated_point[:,0], rotated_point[:,1],  label = "Rotated")

    # Scaled
    scale_x = 1 + ((Scale_factor[0] - 1) * frame) / 100
    scale_y = 1 + ((Scale_factor[1] - 1) * frame) / 100
    
    scaled_points = scale(points, scale_x, scale_y)    
    ax.plot(scaled_points[:, 0], scaled_points[:, 1],label="Scaled")

    ax.legend()

animation = FuncAnimation(
    fig,
    update,
    frames=100,
    interval = 50,
    repeat = False
)

plt.show()