import tkinter as tk
import time
from widgets import Boton_menu

class Main(tk.Tk):
	"""Root class"""

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		# Configuracion de la ventana principal

		#Titulo ventana
		tit = "Bar La biela " + time.ctime()
		self.title(tit)

		# Side frame
		self.menuLateral = Lateral(self)
		self.menuLateral.grid(column=0, row=0, rowspan=2, sticky='nsew')

		# Control frame
		self.menuIngreso = Ingreso(self)
		self.menuIngreso.grid(column=1, row=0, sticky=tk.NSEW)


class Lateral(tk.Frame):
	"""Frame del menu lateral"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, width=200, height=800, bd=30)
		self.botMenu = self.crea_bot(self)

	def crea_bot(self):
		lista_bot = []
		

class Ingreso(tk.Frame):
	"""Frame de ingreso"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
