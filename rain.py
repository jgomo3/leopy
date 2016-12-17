#!/usr/bin/env python3

import math
import random
import tkinter as tk

class Drop():

    def __init__(self, canvas, left, top, depth, color, bottom=400, right=400):
        self.__canvas = canvas
        self.__left = left
        self.__top = top
        self.__depth = depth
        self.__color = color
        self.__bottom = bottom
        self.__right = right

        self.__initial_vx = 0
        self.__initial_vy = 5
        self.__initial_height = 5
        self.__initial_width = 1
        self.__initial_depth = 0

        self.__scale()

        self.__id = canvas.create_line(
            self.__left,
            self.__top,
            self.__left,
            self.__top + self.__height,
            width=self.__width,
            fill=self.__color
        )

    def __scale(self):
        delta = self.__depth - self.__initial_depth

        # Affected
        factor = (delta - 5)**2 / 10
        self.__height = factor * self.__initial_height
        self.__vy = factor * self.__initial_vy
        self.__width = factor * self.__initial_width

        # Constants -> 1
        self.__vx = 1 * self.__initial_vx

    def move(self):
        if self.__canvas.coords(self.__id)[1] > self.__bottom:
            self.__canvas.coords(self.__id, self.__left, 0, self.__left, self.__height)
        else:
            self.__canvas.move(self.__id, self.__vx, self.__vy)

class App():

    def __init__(self, master, width=400, height=400, max_depth=5, population=50):
        self.__master = master
        self.__width = width
        self.__height = height
        self.__max_depth = max_depth
        self.__population = population
        self.__canvas = tk.Canvas(
            self.__master,
            width=self.__width,
            height=self.__height)
        self.__objects = self.__load_objects(canvas=self.__canvas)
        self.__canvas.pack()
        self.__master.after(0, self.__animation)

    def __animation(self):
        for _object in self.__objects:
            _object.move()
        self.__master.after(120, self.__animation)

    def __load_objects(self, canvas):
        return [
            Drop(canvas=canvas, left=left, top=top, depth=depth, color='blue', bottom=self.__height, right=self.__width)
            for left, top, depth in
            (
                (
                    random.randrange(0, upper)
                    for upper in (
                        self.__width,
                        self.__height,
                        self.__max_depth
                    )
                )
                for _ in range(self.__population)
            )
        ]


root = tk.Tk()
app = App(master=root, population=100)
root.mainloop()