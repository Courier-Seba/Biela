#####
# Modulos de los frames principales, excluidos los root y el lateral
####
import tkinter as tk
from widgets import Titulo, BotonIngreso, EntradaIngreso
from carga import listaDeProductos


class Pedido(tk.Frame):
	"""Frame de ingreso"""

	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#FFFFFF")
		self.parent = parent
		self.widIngreso = []
		self.crea_wid()
		

	def crea_wid(self):
		self.titulo = Titulo(self, "Orden de pedido")
		self.titulo.grid(column=0, row=0, columnspan=99)

		for prod in listaDeProductos:
			widEnt = EntradaIngreso(self)
			widBut = BotonIngreso(self, prod.nombre, widEnt)
			par = [widEnt, widBut]
			self.widIngreso.append(par)

		rowLevel = 1
		for wid in self.widIngreso:
			wid[1].grid(column=0, row=rowLevel)
			wid[0].grid(column=1, row=rowLevel)
			rowLevel += 1


class Clientes(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#0000FF")
		self.parent = parent
		self.crea_wid()

	def crea_wid(self):
		self.titulo = Titulo(self, "Clientes")
		self.titulo.grid(column=0, row=0, columnspan=99)



class Productos(tk.Frame):
	"""Frame de vista e ingreso de productos"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#FFFFFF")
		self.parent = parent
		self.crea_wid()

	def crea_wid(self):
		self.titulo = Titulo(self, "Productos")
		self.titulo.grid(column=0, row=0, columnspan=99)

		self.subTit = Titulo(self, "Ingreso nuevo producto")
		self.subTit.grid(column=0, row=1)

		


class Estadisticas(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#0000FF")
		self.parent = parent
		self.label = tk.Label(self, text="", bg="#00FF00")
		self.label.pack()
