import math
import random
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

N = 70  ### 스텝 횟수
F = 20
B = 10
Nx = np.random.random(N)  ### [0,1] 사이에서 균등 분포를 갖는 무작위 변수 N개 생성
Ny = np.random.random(N)

### X의 초기값 x_0 = 0으로 정의하고 수열에 포함


Fx = np.random.random(F)  ### [0,1] 사이에서 균등 분포를 갖는 무작위 변수 N개 생성
Fy = np.random.random(F)

### X의 초기값 x_0 = 0으로 정의하고 수열에 포함


Bx = np.random.random(B)  ### [0,1] 사이에서 균등 분포를 갖는 무작위 변수 N개 생성
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

            elif norm(Nx[i], Ny[i], Fx[j], Fy[j]) <= 0.05:
                Nx = np.append(Nx, random.randrange(0, 1))
                Ny = np.append(Ny, random.randrange(0, 1))

            elif norm(Fx[j], Fy[j], Bx[k], By[k]) <= 0.05:
                Fx = np.delete(Fx, k)
                Fy = np.delete(Fy, k)

plt.plot(Nx, Ny, marker='o', markersize=3, lw=1)

plt.plot(Fx,Fy, marker='o', markersize=3, lw=1)

plt.plot(Bx, By, marker='o', markersize=3, lw=1)

plt.xlabel('x_n')
plt.ylabel('y_n')
plt.show()  ### 결과를 그래프로 출력
