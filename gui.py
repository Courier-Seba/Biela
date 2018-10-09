import tkinter as tk
import time
from widgets import Boton_agrega

class Window(tk.Tk):
	"""Root class"""

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		# Configuracion de la ventana principal
		#Titulo ventana
		tit = "Bar La biela " + time.ctime()
		self.title(tit)

		# Main Frame
		self.mainFrame = Main(self)
		self.mainFrame.grid()

class Main(tk.Frame):
	"""Frame mas bajo, sobre el se crean los demas"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#FFFFFF")
		self.parent = parent

		self.lateral = Lateral(self)
		self.lateral.grid(column=0, row=0)

		self.container = tk.Frame()
		self.container.grid(column=1, row=0)


class Lateral(tk.Frame):
	"""Frame del menu lateral"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#000000", bd=10)
		self.parent = parent
		# Crea botones
		self.botMenu = self.crea_bot()
		# Los ubica
		for bot in self.botMenu:
			bot.pack(side=tk.TOP, fill=tk.X, expand=True)

	def crea_bot(self):
		botones = []
		#Cantidad de botones (len de la lista) y sus textos
		nombresBotones = ["Toma pedido", "Clientes", "Productos",
						  "Estadisticas"]

		for name in nombresBotones:
			bot = Boton_agrega(self, name)
			botones.append(bot)
		return botones
