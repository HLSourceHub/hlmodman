#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from mgenui import mgenUI


class mgen(mgenUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = mgen()
    app.run()
