import tkinter as tk
from widgets import Titulo, BotonIngreso, EntradaIngreso, Texto


class Clientes(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#0000FF")
		self.parent = parent
		self.crea_wid()

	def crea_wid(self):
		self.titulo = Titulo(self, "Clientes")
		self.titulo.grid(column=0, row=0, columnspan=99)