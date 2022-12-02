import random
import sys
from tkinter.ttk import Entry

import tkinter as tki
import matplotlib.pyplot as mat
import simpy as sim
import numpy as np

window = tki.Tk()
window.title("GameTheorySimulation")
window.resizable(True, True)
lbl1 = tki.Label(window, text="전체 모집단 수")
lbl1.pack()
whole_size = tki.Entry(window, width=30)
whole_size.pack()
lbl2 = tki.Label(window, text="선심파 수")
lbl2.pack()
number_of_friendly = tki.Entry(window, width=30)
number_of_friendly.pack()
lbl3 = tki.Label(window, text="나이스파 수")
lbl3.pack()
number_of_nice = tki.Entry(window, width=30)
number_of_nice.pack()
lbl4 = tki.Label(window, text="사기꾼 파 수")
lbl4.pack()
number_of_bad = tki.Entry(window, width=30)
number_of_bad.pack()

window.mainloop()

if whole_size.pack() > 1000:
    print("수가 너무 큽니다.")
    sys.exit()
else:
    prob_set = [(number_of_friendly / whole_size) * (number_of_nice / whole_size),
                (number_of_nice / whole_size) * (number_of_bad / whole_size),
                (number_of_friendly / whole_size) * (number_of_bad / whole_size)]

    positionX = []
    positionY = []
    for x in range(1000):
        positionX.append(random.randint(1,1000))
    for y in range(1000):
        positionY.append(random.randint(1, 1000))

