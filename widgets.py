####
# La funcion de este modulo es personalizar los widgets aparte para mejor
# control y facil modificacion.
####


import tkinter as tk

class Boton_menu(tk.Button):
	"""Boton del menu lateral"""

	def __init__(self, master, texto, controller):
		tk.Button.__init__(self, master, background="#FFFFFF",
						   foreground="#000000", text=texto,
						   activebackground="#0000FF",
						   command=lambda: controller.carga_frame(texto))


class Titulo(tk.Label):
	"""Label para tituloso"""

	def __init__(self, master, texto):
		tk.Label.__init__(self, master, text=texto, bg="#FF0000")

class Boton_ingreso(tk.Button):
	"""Boton de ingreso"""

	def __init__(self, master, texto, controller):
		tk.Button.__init__(self, master, text=texto,
						   command=lambda: print("hi"))
