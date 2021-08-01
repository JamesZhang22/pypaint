from tkinter import *
from tkinter import colorchooser
from typing import Tuple

def choose_color() -> Tuple:
    root = Tk()
    root.withdraw()
    root.title("")
    root.geometry("400x400")
    my_color = colorchooser.askcolor()
    color = []
    for rgb in my_color[0]:
        color.append(round(int(rgb)))

    return tuple(color)


    my_button = Button(root, text="Pick a Color", command=choose_color).pack()

    root.mainloop()
