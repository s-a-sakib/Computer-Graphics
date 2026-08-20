import matplotlib.pyplot as plt

# Rectangular clipping window
xmin, ymin = 2, 2
xmax, ymax = 8, 7

#Region Code (TBRL)

TOP    = 8 #1000
BOTTOM = 4 #0100
RIGHT  = 2 #0010
LEFT   = 1 #0001
INSIDE = 0 #0000

def Compute_Code(x,y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

def Cohen_Sutherland(x1, y1, x2, y2):
    code1 = Compute_Code(x1,y1)
    code2 = Compute_Code(x2,y2)

    while True:

        #Both are inside
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2       
        # Both points share an outside region
        elif code1 & code2:
            return None

        # Line is partially inside
        else:

            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1)/(y2 - y1)
                y = ymax

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1)/(y2 - y1)
                y = ymin

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1)/(x2 - x1)
                x = xmax

            elif code_out & LEFT:

                y = y1 + (y2 - y1) * (xmin - x1)/(x2 - x1)
                x = xmin

            # Replace outside point
            if code_out == code1:
                x1 = x
                y1 = y

                code1 = Compute_Code(
                    x1, y1
                )
            else: 
                x2 = x
                y2 = y

                code2 = Compute_Code(
                    x2, y2
                )

# Original line
x1, y1 = 0, 1
x2, y2 = 10, 8

# Call only once
result = Cohen_Sutherland(x1, y1, x2, y2)


# Draw original line
plt.plot(
    [x1, x2],
    [y1, y2],
    "--",
    label="Original Line"
)

# Draw clipping window
plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    label="Clipping Window"
)


# Draw clipped line
if result:

    cx1, cy1, cx2, cy2 = result

    plt.plot(
        [cx1, cx2],
        [cy1, cy2],
        linewidth=3,
        label="Clipped Line"
    )



plt.xlim(-1, 11)
plt.ylim(0, 9)

plt.grid()
plt.legend()
plt.gca().set_aspect("equal")

plt.show()