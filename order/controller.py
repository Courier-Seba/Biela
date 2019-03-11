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

# Solo pata testing
productos = ListaProductos(listaDeProductos)
