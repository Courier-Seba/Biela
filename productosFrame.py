import tkinter as tk
from widgets import Titulo, BotonIngreso, EntradaIngreso, Texto
from gestion import productos

class Productos(tk.Frame):
	"""Frame de vista e ingreso de productos"""

	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#FFFFFF")
		self.parent = parent
		self.crea_wid()

	def crea_wid(self):
		self.titulo = Titulo(self, "Productos")
		self.titulo.grid(column=0, row=0, columnspan=99)

		# Nuevo producto
		self.subTitIngre = Titulo(self, "Ingreso nuevo producto")
		self.subTitIngre.grid(column=0, row=1)

		self.labelNuevo = Texto(self, "Nombre")
		self.labelNuevo.grid(column=0, row=2)
		self.ingreNuevo = EntradaIngreso(self)
		self.ingreNuevo.grid(column=1, row=2)

		# Lista de productos
		self.subTitVista = Titulo(self, "Productos")
		self.subTitVista.grid(column=0, row=5)

		# Vista