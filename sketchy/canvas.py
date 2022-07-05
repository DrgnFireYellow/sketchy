from tkinter import Tk
from tkinter import Canvas
class Drawing:
    def __init__(self, width, height):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=width, height=height)
        self.canvas.pack()
    def line(self, x1, y1, x2, y2, color='black'):
        self.canvas.create_line(x1, y1, x2, y2, color=color)
    def rect(self, x1, y1, x2, y2, color='black'):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)