import tkinter as tk
from widgets import Titulo, BotonIngreso, EntradaIngreso, Texto

class Estadisticas(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#0000FF")
		self.parent = parent
		self.label = tk.Label(self, text="", bg="#00FF00")
		self.label.pack()
