#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from SourceHubModManui import asdUI


class asd(asdUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = asd()
    app.run()
