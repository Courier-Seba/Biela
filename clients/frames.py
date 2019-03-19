import tkinter
from .widgets import Titulo, BotonIngreso, EntradaIngreso, Texto


class ClientsFrame(tkinter.Frame):
    """ Frame of Clients management """
    def __init__(self, parent):
        super().__init__(parent, bg="#0000FF")
        self.parent = parent
        self.crea_wid()

    def crea_wid(self):
        self.titulo = Titulo(self, "Clientes")
        self.titulo.grid(column=0, row=0, columnspan=99)
