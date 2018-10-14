#####
# Modulos de los frames principales, excluidos los root y el lateral
####
import tkinter as tk
from widgets import Titulo, Boton_ingreso

class Pedido(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#30FFFF")
		self.parent = parent
		self.crea_wid()

	def crea_wid(self):
		titulo = Titulo(self, "Orden de pedido")
		titulo.grid(column=0, row=0)

		botonCafe = Boton_ingreso(self, "Taza chiquita", self.parent)
		botonCafe.grid(column=0, row=1)

class Clientes(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#0000FF")
		self.parent = parent
		self.label = tk.Label(self, text="", bg="#00FF00")
		self.label.pack()

class Productos(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#0000FF")
		self.parent = parent
		self.label = tk.Label(self, text="", bg="#00FF00")
		self.label.pack()

class Estadisticas(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#0000FF")
		self.parent = parent
		self.label = tk.Label(self, text="", bg="#00FF00")
		self.label.pack()
