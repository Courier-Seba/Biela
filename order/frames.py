import tkinter
from widgets import Titulo, BotonIngreso, EntradaIngreso, Texto
from gestion import productos



class OrderFrame(tkinter.Frame):
        """Frame de ingreso"""

        def __init__(self, parent):
                super().__init__(parent, bg="#FFFFFF")
                self.parent = parent
                self.widIngreso = []
                self.crea_wid()

        def crea_wid(self):
                self.titulo = Titulo(self, "Orden de pedido")
                self.titulo.grid(column=0, row=0, columnspan=99)

                for prod in productos.lista:
                        widEnt = EntradaIngreso(self)
                        widBut = BotonIngreso(self, prod.nombre, widEnt)
                        par = [widEnt, widBut]
                        self.widIngreso.append(par)

                rowLevel = 1
                for wid in self.widIngreso:
                        wid[1].grid(column=0, row=rowLevel)
                        wid[0].grid(column=1, row=rowLevel)
                        rowLevel += 1
