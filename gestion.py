#####
# Clases de gestion
#####

import pickle

class Orden:
        """Orden del cliente"""

        def __init__(self, mesa, cliente, listaProductos, estado):
                self.mesa = mesa
                self.cliente = cliente
                self.productos = listaProductos
                self.total = self.calculo_total()

                # Inpaga paga
                self.estado = estado

        def calculo_total(self):
                for prod in self.productos:
                        final += prod.precio
                
                return final


class Mesa:
        """Mesa y su ubicacion"""

        def __init__(self):
                self.descripcion = ""


class Cliente:
        """Plantilla de datos cliente"""

        def __init__(self):
                self.nombre = ""
                self.apellido = ""
                self.direccion = ""
                self.tel = 0 
                # ids de ordenes
                self.cuentaCorriente = []

        def deuda_total(self):
                for compra in self.cuentaCorriente:
                        if compra.estado == False:
                                deuda += compra.total

                return deuda


class Producto:
        """Producto de venta"""

        def __init__(self, nombre, desc, precio):
                self.nombre = nombre
                self.descripcion = desc
                self.precio = precio
                # Es una salida para la muestra de la info

        def formateo_textual(self):
                textoFinal = ""
                for atr in [self.nombre, self.descripcion, self.precio]:
                        textoFinal += atr + "\n"
                return textoFinal

class ListaProductos:
        """Productos de una orden"""

        def __init__(self, productos):
                # Lista de ids de productos
                self.nombreArchivo = "save.p"
                self.lista = productos

        def carga_data(self):
                with open(self.nombreArchivo, "rb") as file:
                        carga = pickle.load(file)

                return carga

        def guarda_data(self):
                with open(self.nombreArchivo, "wb") as file:
                        pickle.dump(self.lista, file)

listaDeProductos = [
        Producto("Cafe", "chico", "30"),
        Producto("cafeLeche", "taza", "50")
]

productos = ListaProductos(listaDeProductos)
