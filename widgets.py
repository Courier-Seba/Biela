import tkinter as tk

class Boton_agrega(tk.Button):
	"""Boton del menu lateral"""

	def __init__(self, parent, texto):
		tk.Button.__init__(self, parent, backgroun="#FFFFFF",
		                   foreground="#000000", text=texto, 
		                   activebackground="#0000FF")
