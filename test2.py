import math
import numpy as np
import matplotlib.pyplot as plt

F = 700
fl = [700]
B = 300
bl = [300]

Fx = np.random.random(F)
Fy = np.random.random(F)

Bx = np.random.random(B)
By = np.random.random(B)


def norm(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


for n in range(1, F):
    r = Fx[n]
    q = Fy[n]
    x_prev = Fx[n - 1]
    y_prev = Fy[n - 1]
    if r <= 1 / 2 and q <= 1 / 2:
        x_next = x_prev + 1
        y_next = y_prev + 1
    elif r > 1 / 2 >= q:
        x_next = x_prev - 1
        y_next = y_prev + 1
    elif r <= 1 / 2 < q:
        x_next = x_prev + 1
        y_next = y_prev - 1
    else:
        x_next = x_prev - 1
        y_next = y_prev - 1

    Fx = np.append(Fx, x_next)
    Fy = np.append(Fy, y_next)

for n in range(1, B):
    r = Bx[n]
    q = By[n]
    x_prev = Bx[n - 1]
    y_prev = By[n - 1]
    if r <= 1 / 2 and q <= 1 / 2:
        x_next = x_prev + 1
        y_next = y_prev + 1
    elif r > 1 / 2 >= q:
        x_next = x_prev - 1
        y_next = y_prev + 1
    elif r <= 1 / 2 < q:
        x_next = x_prev + 1
        y_next = y_prev - 1
    else:
        x_next = x_prev - 1
        y_next = y_prev - 1

    Bx = np.append(Bx, x_next)
    By = np.append(By, y_next)
for i in range(0, 700):
    for j in range(0, 300):
        if norm(Fx[i], Fy[i], Bx[j], By[j]) <= 0.05:
            F -= 1
            B += 1
            fl.append(F)
            bl.append(B)

plt.plot(fl, marker='o', markersize=3, lw=1)
plt.plot(bl, marker='o', markersize=3, lw=1)

print(fl)
print(bl)
plt.show()
