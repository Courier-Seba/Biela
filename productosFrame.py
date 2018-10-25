import tkinter as tk
from widgets import Titulo, BotonIngreso, EntradaIngreso, Texto, BotonLargo
from widgets import MuestraLabel
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
		self.ingreNuevoNom = EntradaIngreso(self)
		self.ingreNuevoNom.grid(column=1, row=2)
		self.labelNuevoPrec = Texto(self, "Descripción")
		self.labelNuevoPrec.grid(column=0, row=3)
		self.ingreNuevoPrec = EntradaIngreso(self)
		self.ingreNuevoPrec.grid(column=1, row=3)
		self.labelNuevoPrec = Texto(self, "Precio")
		self.labelNuevoPrec.grid(column=0, row=4)
		self.ingreNuevoPrec = EntradaIngreso(self)
		self.ingreNuevoPrec.grid(column=1, row=4)

		self.tomaNuevo = BotonLargo(self, "Cancelar")
		self.tomaNuevo.grid(column=0, row=5, sticky=tk.NSEW)
		self.tomaNuevo = BotonLargo(self, "Agregar")
		self.tomaNuevo.grid(column=1, row=5, sticky=tk.NSEW)

		# Lista de productos
		self.subTitVista = Titulo(self, "Productos")
		self.subTitVista.grid(column=0, row=6)

		# Vista
		# Crea labels de cada producto
		self.infoDeProductos = []
		for prod in productos.lista:
			cont = prod.formateo_textual()
			infoProducto = MuestraLabel(self, cont)
			self.infoDeProductos.append(infoProducto)

		# Pocisiona
		ultimoLugarDisponible = 7
		for numLabel in range(len(self.infoDeProductos)):
			self.infoDeProductos[numLabel].grid(column=0, 
												row = ultimoLugarDisponible)
			ultimoLugarDisponible += 1

