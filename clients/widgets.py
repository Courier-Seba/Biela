import tkinter

class Titulo(tkinter.Label):
        """Label para tituloso"""

        def __init__(self, master, texto):
                tkinter.Label.__init__(self, master, text=texto, bg="#FF0000")

class BotonIngreso(tkinter.Button):
        """Boton de ingreso"""

        def __init__(self, master, texto, controller):
            tkinter.Button.__init__(
                self, master, text=texto,
                command=lambda: controller.inserta_uno()
            )

class EntradaIngreso(tkinter.Entry):
        """Entrada de la cantidad de X productos."""

        def __init__(self, master):
            tkinter.Entry.__init__(self, master, bg="#FFFFFF", fg="#000000")
            self.insert(0, "0")

        def inserta_uno(self):
            cantActual = self.toma_dato()
            cantFinal = cantActual + 1
            self.delete(0, tkinter.END)
            self.insert(0, str(cantFinal))

        def toma_dato(self):
            dato = self.get()
            try:
                datoInt = int(dato)
            except:
                ValueError: print("U miss")
            return datoInt

class Texto(tkinter.Label):
        """Texto comun"""

        def __init__(self, master, muestraTexto):
                tkinter.Label.__init__(
                    self, master, bg="#FFFFFF", fg="#000000", 
                    text=muestraTexto
                )


