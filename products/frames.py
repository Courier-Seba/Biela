import tkinter

from . import widgets
from .config import Config

from gestion import productos

class ProductsFrame(tkinter.Frame):
    """Frame de vista e ingreso de productos"""

    def __init__(self, parent):
        super().__init__(parent, bg="#FFFFFF")
        self.parent = parent
        self.start_widgets()

    def start_widgets(self):
        self.title = widgets.Title(self, Config.FRAME_TITLE)
        self.title.grid(column=0, row=0, columnspan=99)

        # Nuevo producto
        self.sub_tit = widgets.Title(self, "Ingreso nuevo producto")
        self.sub_tit.grid(column=0, row=1)

        self.labelNuevo = widgets.TextLabel(self, "Nombre")
        self.labelNuevo.grid(column=0, row=2)
        self.ingreNuevoNom = widgets.AddButton(self)
        self.ingreNuevoNom.grid(column=1, row=2)
        self.labelNuevoPrec = widgets.TextLabel(self, "Descripción")
        self.labelNuevoPrec.grid(column=0, row=3)
        self.ingreNuevoPrec = widgets.AddButton(self)
        self.ingreNuevoPrec.grid(column=1, row=3)
        self.labelNuevoPrec = widgets.TextLabel(self, "Precio")
        self.labelNuevoPrec.grid(column=0, row=4)
        self.ingreNuevoPrec = widgets.AddButton(self)
        self.ingreNuevoPrec.grid(column=1, row=4)

        self.tomaNuevo = widgets.LargeButton(self, "Cancelar")
        self.tomaNuevo.grid(column=0, row=5, sticky=tkinter.NSEW)
        self.tomaNuevo = widgets.LargeButton(self, "Agregar", operacion='print("hola")' )
        self.tomaNuevo.grid(column=1, row=5, sticky=tkinter.NSEW)

        # Lista de productos
        self.subTitVista = widgets.Titulo(self, "Productos")
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
            self.infoDeProductos[numLabel].grid(
                column=0,
                row = ultimoLugarDisponible
            )
            ultimoLugarDisponible += 1

class NewProductFrame(tkinter.Frame):
    """ Frame for adding products """

    def __init__(self, parent):
        super().__init__(parent, bg="#FFFFFF")
        self.parent = parent
        self.load_widgets()


    def load_widgets(self):
        self.title = widgets.TitleLabel(self, Config.FRAME_TITLE)
        self.title.grid(column=0, row=0, columnspan=99)

        self.labelNuevo = widgets.TextLabel(self, "Nombre")
        self.labelNuevo.grid(column=0, row=2)
        self.labelNuevoPrec = widgets.TextLabel(self, "Descripción")
        self.labelNuevoPrec.grid(column=0, row=3)
        self.labelNuevoPrec = widgets.TextLabel(self, "Precio")
        self.labelNuevoPrec.grid(column=0, row=4)

        self.tomaNuevo = widgets.LargeButton(self, "Cancelar")
        self.tomaNuevo.grid(column=0, row=5, sticky=tkinter.NSEW)
        self.tomaNuevo = widgets.LargeButton(self, "Agregar")
        self.tomaNuevo.grid(column=1, row=5, sticky=tkinter.NSEW)

class ListProductsFrame(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.load_widgets()

    def load_widgets(self):
        self.title = widgets.TitleLabel(self, "Productos")
        self.title.grid(column=0, row=6)

        # Crea labels de cada producto
        self.infoDeProductos = []
        for prod in productos.lista:
            cont = prod.formateo_textual()
            infoProducto = widgets.BoxedLabel(self, cont)
            self.infoDeProductos.append(infoProducto)

        # Pocisiona
        ultimoLugarDisponible = 7
        for numLabel in range(len(self.infoDeProductos)):
            self.infoDeProductos[numLabel].grid(
                column=0,
                row = ultimoLugarDisponible
            )
            ultimoLugarDisponible += 1
