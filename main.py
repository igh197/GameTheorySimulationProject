import random
import sys
from tkinter.ttk import Entry

import tkinter as tki
import matplotlib.pyplot as plt
import simpy as sim
import numpy as np

window = tki.Tk()
window.title("GameTheorySimulation")
window.resizable(True, True)

lbl1 = tki.Label(window, text="전체 모집단 수")
lbl1.pack()

whole_size = tki.Entry(window, width=30)
whole = whole_size.get()
whole_size.pack()
buttonW = tki.Button("입력")

lbl2 = tki.Label(window, text="선심파 수")
lbl2.pack()

number_of_friendly = tki.Entry(window, width=30)
friendly = number_of_friendly.get()
number_of_friendly.pack()

lbl3 = tki.Label(window, text="나이스파 수")
lbl3.pack()

number_of_nice = tki.Entry(window, width=30)
nice = number_of_nice.get()
number_of_nice.pack()

lbl4 = tki.Label(window, text="사기꾼 파 수")
lbl4.pack()

number_of_bad = tki.Entry(window, width=30)
bad = number_of_bad.get()
number_of_bad.pack()

positionX = []
positionY = []
for x in range(1000):
    positionX.append(int(random.randrange(1, whole)))
for y in range(1000):
    positionY.append(int(random.randrange(1,whole)))
for x in range(1000):
    positionX.append(int(random.randrange(1,nice)))
for y in range(1000):
    positionY.append(int(random.randrange(1,nice)))
for x in range(1000):
    positionX.append(int(random.randrange(1,friendly)))
for y in range(1000):
    positionY.append(int(random.randrange(1,friendly)))
for x in range(1000):
    positionX.append(int(random.randrange(1,bad)))
for y in range(1000):
    positionY.append(int(random.randrange(1,bad)))

plt.scatter(positionX, positionY)
plt.show()

window.mainloop()
