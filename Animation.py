import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def Translate(points, tx, ty):
    return points + [tx, ty]


def Rotate(points, angle):
    angle_rad = np.radians(angle)
    rotated = []
    
    for x, y in points:
        r = np.sqrt(x**2 + y**2)
        angle1 = np.arctan2(y, x)      # handles all quadrants + x=0
        x_new = r * np.cos(angle1 + angle_rad)
        y_new = r * np.sin(angle1 + angle_rad)
        rotated.append([x_new, y_new])
    
    return np.array(rotated)


def Scale(points, sx, sy):
    return points * [sx, sy]


points = np.array([
    [1, 1],
    [4, 1],
    [2.5, 4],
    [1, 1]
])

translation = (5, 5)
angle = 60
Scale_factor = (3, 4)

fig, ax = plt.subplots(figsize=(8, 8))


def update(frame):

    ax.clear()

    ax.set_xlim(-10, 20)
    ax.set_ylim(-10, 20)
    ax.grid()
    ax.set_title("2D Transformations")

    # Original
    ax.plot(
        points[:, 0],
        points[:, 1],
        'bo-',
        label="Original"
    )
    # Translated
    moving_points = Translate(points, translation[0] * frame / 100, translation[1] * frame / 100)   
    ax.plot(
        moving_points[:, 0],
        moving_points[:, 1],
        'ro-',
        label="Translated"
    )


    # Rotated
    rotated_points = Rotate(points, angle * frame / 100)
    ax.plot(
        rotated_points[:, 0],
        rotated_points[:, 1],
        'go-',
        label="Rotated"
    )


    # Scaled
    scale_x = 1 + (Scale_factor[0] - 1) * frame / 100
    scale_y = 1 + (Scale_factor[1] - 1) * frame / 100

    scaled_points = Scale(points, scale_x, scale_y)    
    ax.plot(
            scaled_points[:, 0],
            scaled_points[:, 1],
            'mo-',
            label="Scaled"
        )

    ax.legend()

ani = FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50,
    repeat=False
)

plt.show()