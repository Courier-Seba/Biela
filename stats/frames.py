import tkinter
from .widgets import Titulo, BotonIngreso, EntradaIngreso, Texto

class StatsFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0000FF")
        self.parent = parent
        self.label = tkinter.Label(self, text="", bg="#00FF00")
        self.label.pack()
