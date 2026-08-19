import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def brezenham_line(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    points = []

    while True:

        points.append([x1, y1])

        if x1 == x2 and y1 == y2:
            break

        err2 = 2 * err

        if err2 > -dy:
            err = err - dy
            x1 += sx

        if err2 < dx:
            y1 += sy
            err += dx

    return points


# Generate line points
line_points = brezenham_line(2, 3, 12, 9)


# Create figure
fig, ax = plt.subplots(figsize=(10, 10))

ax.set_xlim( 0, 14)
ax.set_ylim(0, 14)

ax.set_aspect("equal")


line, = ax.plot([], [], 'bo-', linewidth=2)

title = ax.set_title("Bresenham Line Drawing")


def update(frame):

    points = np.array(line_points[:frame + 1])

    line.set_data(points[:, 0], points[:, 1])

    title.set_text(
        f"Bresenham Line Drawing - Point {frame + 1}"
    )

    return line, title


animation = FuncAnimation(
    fig,
    update,
    frames=len(line_points),
    interval=1000,
    repeat=False
)
plt.grid(True)
plt.show()