import numpy as np
import matplotlib.pyplot as plt

def brezenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    prints = []

    while True:
        prints.append([x1, y1])

        if x1 == x2 and y1 == y2:
            break

        err2 = 2 * err

        if err2 > -dy:
            err = err - dy
            x1 += sx

        if err2 < dx:
            err = err + dx
            y1 += sy

    return prints

# points = brezenham_line(2, 3, 12, 9)

# print("Line Points:\n", points)


# plt.plot([p[0] for p in points], [p[1] for p in points], 'bo-')
# plt.title("Bresenham's Line Drawing Algorithm")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid()
# plt.show()