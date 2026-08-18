import matplotlib.pyplot as plt

# Rectangular clipping window
xmin, ymin = 2, 2
xmax, ymax = 8, 7

def inside(p1, edge):
    x , y = p1

    if edge == "left":
        return x >= xmin
    elif edge == "right":
        return x <= xmax
    elif edge == "top":
        return y <= ymax
    else:
        return y >= ymin

def intersection(p1, p2, boundary):
    x1 , y1 = p1
    x2 , y2 = p2

    if boundary == "left":
        x = xmin
        y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)

    elif boundary == "right":
        x = xmax
        y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)

    elif boundary == "bottom":
        y = ymin
        x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

    elif boundary == "top":
        y = ymax
        x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

    return (x, y) 

# Sutherland-Hodgman Algorithm
def clip_polygon(polygon):
    boundaries = ["left","right","bottom","top"]
    output = polygon

    for boundary in boundaries:

        input_polygon = output
        output = []

        if not input_polygon:
            break

        s = input_polygon[-1]

        for p in input_polygon:
            if inside(p, boundary):
                if not inside(s, boundary):
                    output.append(intersection(s, p, boundary))
                output.append(p)
            elif inside(s, boundary):
                output.append(intersection(s, p, boundary))
            s = p
    return output   


# Polygon
polygon = [
    (1, 3),
    (5, 9),
    (10, 6),
    (7, 1),
    (3, 1)
]


# Clip polygon
clipped = clip_polygon(polygon)

print("Original Polygon:")
print(polygon)

print("\nClipped Polygon:")
print(clipped)

# Draw result
plt.figure()

# Original polygon
original = polygon + [polygon[0]]
x, y = zip(*original)
plt.plot(x, y, 'b--', label="Original")

# Clipped polygon
if clipped:
    clipped_closed = clipped + [clipped[0]]
    x, y = zip(*clipped_closed)
    plt.plot(x, y, 'r-', label="Clipped")

# Clipping window
window_x = [xmin, xmax, xmax, xmin, xmin]
window_y = [ymin, ymin, ymax, ymax, ymin]

plt.plot(window_x, window_y, 'k-', label="Clipping Window")

plt.xlim(0, 11)
plt.ylim(0, 10)
plt.grid()
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Sutherland-Hodgman Polygon Clipping")

plt.show()