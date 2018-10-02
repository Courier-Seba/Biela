import tkinter as tk

class Boton_menu(tk.Button):
	"""Boton del menu lateral"""

	def __init__(self, parent, text):
		tk.Button.__init__(self, parent, backgroun="#FFFFFF")
