from tkinter.ttk import Entry

import tkinter as tki
import matplotlib as mat
import simpy as sim
import numpy as np

window = tki.Tk()
window.title = "GameTheorySimulation"
window.resizable(True, True)


def simulation_community(whole_size, number_of_friendly, number_of_nice, number_of_bad):
    whole_size = tki.Entry(window, width=30)
    number_of_friendly = tki.Entry(window, width=30)
    number_of_nice = tki.Entry(window, width=30)
    number_of_bad = tki.Entry(window, width=30)
