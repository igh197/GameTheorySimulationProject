import math
import random
import numpy as np
import matplotlib.pyplot as plt

N = 70
nl = [70]
F = 20
fl = [20]
B = 10
bl = [10]
Nx = np.random.random(N)
Ny = np.random.random(N)

Fx = np.random.random(F)
Fy = np.random.random(F)

Bx = np.random.random(B)
By = np.random.random(B)


def norm(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


for n in range(1, N):
    r = Nx[n]
    q = Ny[n]
    x_prev = Nx[n - 1]
    y_prev = Ny[n - 1]
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
    Nx = np.append(Nx, x_next)
    Ny = np.append(Ny, y_next)

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
for i in range(0, 70):
    for j in range(0, 20):
        for k in range(0, 10):
            if norm(Nx[i], Ny[i], Bx[k], By[k]) <= 0.05:
                Bx = np.delete(Bx, k)
                By = np.delete(By, k)
                Nx = np.append(Nx, random.randrange(0, 1))
                Ny = np.append(Ny, random.randrange(0, 1))
                B -= 1
                N += 1
                bl.append(B)
                nl.append(N)
            elif norm(Nx[i], Ny[i], Fx[j], Fy[j]) <= 0.05:
                Nx = np.append(Nx, random.randrange(0, 1))
                Ny = np.append(Ny, random.randrange(0, 1))
                Fx = np.append(Fx, random.randrange(0, 1))
                Fy = np.append(Fy, random.randrange(0, 1))
                N += 1
                nl.append(N)
                F += 1
                fl.append(F)
            elif norm(Fx[j], Fy[j], Bx[k], By[k]) <= 0.05:
                Fx = np.delete(Fx, k)
                Fy = np.delete(Fy, k)
                Bx = np.append(Bx, random.randrange(0, 1))
                By = np.append(By, random.randrange(0, 1))
                F -= 1
                fl.append(F)
                B += 1
                bl.append(B)
plt.plot(nl, marker='o', markersize=3, lw=1)
plt.plot(fl, marker='o', markersize=3, lw=1)
plt.plot(bl, marker='o', markersize=3, lw=1)

print(nl)
print(fl)
print(bl)
plt.show()
