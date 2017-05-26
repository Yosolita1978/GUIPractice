from random import *
from tkinter import *

size = 600
window = Tk()
window.title("First GUI")
canvas = Canvas(window, width=size, height=size)
Label(canvas, text="A bunch of Circles")
canvas.pack()
while True:
    col = choice(["pink", "orange", "purple", "yellow", "blue", "red", "green"])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)

    canvas.create_polygon(
        x0, y0 + 20,
        x0 + 20, y0,
        x0 + 20, y0 - 10,
        x0 + 10, y0 - 20,
        x0, y0 - 10,
        x0 - 10, y0 - 20,
        x0 - 20, y0 - 10,
        x0 - 20, y0,
        fill=col)
    canvas.create_text(300, 300, text="!A bunch of Hearts!", anchor=W, font="Purisa")
    
    window.update()