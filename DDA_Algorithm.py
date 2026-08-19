import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

step = 0

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    step = max(abs(dx), abs(dy))

    x_inc = dx / step
    y_inc = dy / step

    points = []

    if step == 0:
        return np.array([x1, y1])

    for i in range(step + 1):
        points.append([round(x1), round(y1)])
        x1 += x_inc
        y1 += y_inc

    return points

line_points = DDA(2, 3, 12, 9)

print(line_points)

fig , ax = plt.subplots(figsize = (10,10))

ax.set_ylim(0, 14)
ax.set_xlim(0, 14)
ax.set_aspect("equal")

title = ax.set_title("DDA line Drawing Algorithm ")
line,  = ax.plot([],[],'bo-', linewidth = 2)

def update(frame):
    points = np.array(line_points[:frame + 1])
    line.set_data(points[:,0], points[:,1])
    title.set_text(f"DDA line Drawing Algorithm -- {frame}")
    return line, title

animation = FuncAnimation(
    fig,
    update,
    frames= len(line_points) + 1,
    interval = 1000,
    repeat = False
)

plt.grid(True)
plt.show()