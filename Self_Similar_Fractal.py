import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def Koch(p1, p2, n):
    if n == 0:
        return [p1, p2]

    A = p1 + (p2 - p1)/3
    B = p1 + 2*(p2 - p1)/3

    V = B - A
    angle = np.radians(60)

    x = V[0] * np.cos(angle) - V[1] * np.sin(angle)
    y = V[0] * np.sin(angle) + V[1] * np.cos(angle)

    V_rotated = np.array([x, y])

    C = A + V_rotated

    part1 = Koch(p1, A, n - 1)
    part2 = Koch(A, C, n - 1)
    part3 = Koch(C, B, n - 1)
    part4 = Koch(B, p2, n - 1)

    return part1[:-1] + part2[:-1] + part3[:-1] + part4

P1 = np.array([0.0, 0.0])
P2 = np.array([10.0, 0.0])
P3 = np.array([5.0, 8.6603])

max_iteration = 5

fig, ax = plt.subplots(figsize = (10, 10))

ax.set_xlim(-2, 12)
ax.set_ylim(-4, 12)
ax.set_aspect("equal")
ax.axis("off")

line1, = ax.plot([],[], linewidth = 2)
line2, = ax.plot([],[], linewidth = 2)
line3, = ax.plot([],[], linewidth = 2)
title = ax.set_title("Koch Curve -- Iteration 0")


def update(iteration):
    line1_points = np.array(Koch(P1, P3, iteration))
    line1.set_data(line1_points[:,0], line1_points[:,1])
    title.set_text(f"Koch Curve -- Iteration {iteration}")

    line2_points = np.array(Koch(P3, P2, iteration))
    line2.set_data(line2_points[:,0], line2_points[:,1])

    line3_points = np.array(Koch(P2, P1, iteration))
    line3.set_data(line3_points[:,0], line3_points[:,1])

    return line1,line2,line3, title


animation = FuncAnimation(
    fig, 
    update,
    frames= max_iteration + 1,
    interval = 1500,
    repeat = False
)

plt.show()
