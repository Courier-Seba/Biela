import tkinter as tk
import time
from widgets import BotonMenu
from pedidoFrame import Pedido
from clienteFrame import Clientes
from productosFrame import Productos
from estadisticasFrame import Estadisticas

class Window(tk.Tk):
	"""Root class"""

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		# Configuracion de la ventana principal
		# Titulo ventana
		tit = "Bar La biela " + time.ctime()
		self.title(tit)
		# Size
#		self.winSize = X + "x" + Y
#		self.geometry(self.winSize)

		self.configure(background="#FFFFFF")

		# Main Frame
		self.mainFrame = Main(self)
		self.mainFrame.pack()

class Main(tk.Frame):
	"""Frame mas bajo, sobre el se crean los demas"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#FFFFFF")
		self.parent = parent

		self.lateral = Lateral(self)
		self.lateral.pack(side=tk.LEFT, fill=tk.Y)

		self.container = tk.Frame()
		self.container.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
		self.frameList = {}

		for Frame in (Bienvenida, Pedido, Clientes, Productos, Estadisticas):
			page_name = Frame.__name__
			frameCreado = Frame(parent=self.container)
			self.frameList[page_name] = frameCreado
			frameCreado.grid(row=0, column=0, sticky="nsew")

		self.carga_frame("Bienvenida")

	def carga_frame(self, page_name):
		'''Carga el frame dado'''
		frame = self.frameList[page_name]
		frame.tkraise()

class Lateral(tk.Frame):
	"""Frame del menu lateral"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#FFFFFF")
		self.parent = parent
		# Crea botones
		self.botMenu = self.crea_bot()
		# Los ubica
		for bot in self.botMenu:
			bot.pack(side=tk.TOP, fill=tk.X)

	def crea_bot(self):
		botones = []
		#Cantidad de botones (len de la lista) y sus textos
		nombresBotones = ["Pedido", "Clientes", "Productos",
						  "Estadisticas"]

		for name in nombresBotones:
			bot = BotonMenu(self, name, self.parent)
			botones.append(bot)

		return botones

class Bienvenida(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, bg="#FFFFFF")
		self.parent = parent
		self.label = tk.Label(self, text="Bienvenido")
		self.label.pack(expand=True)
