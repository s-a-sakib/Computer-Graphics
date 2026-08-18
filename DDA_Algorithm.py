import matplotlib.pyplot as plt

def DDA_Line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    points = []
    if steps == 0:
        points.append([round(x1), round(y1)])
        return points

    x , y = x1 , y1

    for i in range(steps):
        points.append([round(x), round(y)])
        x += x_inc
        y += y_inc


    return points

# points = DDA_Line(2, 3, 12, 9)

# print("Line Points:\n", points)


# plt.plot([p[0] for p in points], [p[1] for p in points], 'bo-')
# plt.title("DDA Line Drawing Algorithm")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid()
# plt.show()