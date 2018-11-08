####
# La funcion de este modulo es personalizar los widgets aparte para mejor
# control y facil modificacion.
####


import tkinter as tk

class BotonMenu(tk.Button):
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

class BotonIngreso(tk.Button):
	"""Boton de ingreso"""

	def __init__(self, master, texto, controller):
		tk.Button.__init__(self, master, text=texto,
						   command=lambda: controller.inserta_uno())


class EntradaIngreso(tk.Entry):
	"""Entrada de la cantidad de X productos."""

	def __init__(self, master):
		tk.Entry.__init__(self, master, bg="#FFFFFF", fg="#000000")
		self.insert(0, "0")

	def inserta_uno(self):
		cantActual = self.toma_dato()
		cantFinal = cantActual + 1
		self.delete(0, tk.END)
		self.insert(0, str(cantFinal))

	def toma_dato(self):
		dato = self.get()
		try:
			datoInt = int(dato)
		except:
			ValueError: print("U miss")

		return datoInt

class Texto(tk.Label):
	"""Texto comun"""

	def __init__(self, master, muestraTexto):
		tk.Label.__init__(self, master, bg="#FFFFFF", fg="#000000", 
						  text=muestraTexto)

class BotonLargo(tk.Button):
	"""Boton que llena eje x
		operacion: funcion del controler"""

	# TODO: Falta el controller
	def __init__(self, master, texto, **kwargs):
		tk.Button.__init__(self, master, text=texto, bg="#FFFFFF", fg="#000000",
							command=lambda: self.ejecuta()
						)
		self.master = master
		self.kw = kwargs


	def ejecuta(self):
		for key, value in self.kw.items():
			if (key == "operacion"):
				return getattr(self.master, value)()
		
		return ""


class MuestraLabel(tk.Label):
	"""Label para texto largo y complejo"""

	def __init__(self, master, contenido):
		tk.Label.__init__(self, master, text=contenido, fg="#000000", bd=10, 
						  bg="#FFFFFF")