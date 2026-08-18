import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Koch(p1, p2, n):
    if n == 0:
        return [p1, p2]

    # Devide the line into 3 equal parts
    A = p1 + (p2 - p1)/3
    B = p1 + 2*(p2 - p1)/3

    # Vector for A to B
    V = B - A

    # Rotate V by angle
    angle = np.radians(60)

    x = V[0] * np.cos(angle) - V[1] * np.sin(angle)
    y = V[0] * np.sin(angle) + V[1] * np.cos(angle)

    V_rotated = np.array([x, y])

    # Third point of the triangle
    C = A + V_rotated

    # Recursively apply Koch algorithm
    part1 = Koch(p1, A, n - 1)
    part2 = Koch(A, C, n - 1)
    part3 = Koch(C, B, n - 1)
    part4 = Koch(B, p2, n - 1)

    # Combine all four parts
    return part1[:-1] + part2[:-1] + part3[:-1] + part4

# Starting points
P1 = np.array([0.0, 0.0])
P2 = np.array([10.0, 0.0])

# Maximum iteration
max_iteration = 6


# Create figure
fig, ax = plt.subplots(figsize=(12, 12))

ax.set_xlim(-1, 11)
ax.set_ylim(-3, 4)

ax.set_aspect("equal")
ax.axis("off")

line, = ax.plot([], [], linewidth=2)

title = ax.set_title("Koch Curve - Iteration 0")

def update(iteration):

    # Generate Koch curve for current iteration
    points = np.array(Koch(P1, P2, iteration))

    # Update line
    line.set_data(points[:, 0], points[:, 1])

    # Update title
    title.set_text(f"Koch Curve - Iteration {iteration}")

    return line, title


# Create animation
animation = FuncAnimation(
    fig,
    update,
    frames=max_iteration + 1,
    interval=1500,
    repeat=False
)

plt.show()