import time
import tkinter as tk


class Main(tk.Tk):
    """Root tk"""

    def __init__(root, *args, **kwargs):
        tk.Tk.__init__(root, *args, **kwargs)
        # Configuracion de la ventana principal

        #Titulo ventana
        tit = "Bar La biela " + time.ctime()
        root.title(tit)

        # Crea el obj pedido
        root.pedido = Pedido()

        # Side frame
        root.side_bar = Side_bar(root)
        root.side_bar.grid(column=0, row=0, rowspan=2, sticky='nsew')

        # Control frame
        root.intro_bar = Ingre_bar(root, root.pedido)
        root.intro_bar.grid(column=1, row=0, sticky=tk.NSEW)


class Side_bar(tk.Frame):
    """Side bar"""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=100, background="#A78C71", bd=30)


class Ingre_bar(tk.Frame):

    def __init__(self, parent, ped):
        tk.Frame.__init__(self, parent, background="#272822")
        # Pasa pedido
        self.pedido = ped
        # Entrada de mesa
        self.label_mesa = tk.Label(self, text="Mesa:")
        self.entry_mesa = tk.Entry(self)
        self.label_mesa.grid(column=0, row=0, columnspan=2, sticky=tk.E)
        self.entry_mesa.grid(column=2, row=0, columnspan=2, sticky=tk.W)

        # Toma de pedido
        self.toma_wid()

    def toma_wid(self):

        # Crea Widgets
        self.label_desa = tk.Label(self, text="Desayuno:")
        self.entry_desa = tk.Entry(self)
        self.label_chico = tk.Label(self, text="Chico:")
        self.entry_chico = tk.Entry(self)
        self.label_jarrita = tk.Label(self, text="Jarrita:")
        self.entry_jarrita = tk.Entry(self)
        self.label_taza = tk.Label(self, text="Taza:")
        self.entry_taza = tk.Entry(self)
        self.label_doble = tk.Label(self, text="Doble:")
        self.entry_doble = tk.Entry(self)
        self.label_factura = tk.Label(self, text="Factura:")
        self.entry_factura = tk.Entry(self)
        self.label_choco = tk.Label(self, text="Chocolatada:")
        self.entry_choco = tk.Entry(self)
        self.label_gas = tk.Label(self, text="Gaseosa:")
        self.entry_gas = tk.Entry(self)
        self.label_matete = tk.Label(self, text="Te o mate:")
        self.entry_matete = tk.Entry(self)

        # Coloca Widgets de toma
        self.label_desa.grid(column=0, row=2, sticky=tk.E)
        self.entry_desa.grid(column=1, row=2, sticky=tk.W)
        self.label_chico.grid(column=2, row=2, sticky=tk.E)
        self.entry_chico.grid(column=3, row=2, sticky=tk.W)

        self.label_jarrita.grid(column=0, row=3, sticky=tk.E)
        self.entry_jarrita.grid(column=1, row=3, sticky=tk.W)
        self.label_taza.grid(column=2, row=3, sticky=tk.E)
        self.entry_taza.grid(column=3, row=3, sticky=tk.W)

        self.label_doble.grid(column=0, row=4, sticky=tk.E)
        self.entry_doble.grid(column=1, row=4, sticky=tk.W)
        self.label_factura.grid(column=2, row=4, sticky=tk.E)
        self.entry_factura.grid(column=3, row=4, sticky=tk.W)

        self.label_choco.grid(column=0, row=5, sticky=tk.E)
        self.entry_choco.grid(column=1, row=5, sticky=tk.W)
        self.label_gas.grid(column=2, row=5, sticky=tk.E)
        self.entry_gas.grid(column=3, row=5, sticky=tk.W)

        self.label_matete.grid(column=0, row=6, sticky=tk.E)
        self.entry_matete.grid(column=1, row=6, sticky=tk.W)

        # Widgets de finalizar
        # Crea
        self.toma_but = tk.Button(self, text="Tomar pedido", command=self.tomar)
        self.canc_but = tk.Button(self, text="Cancelar", command=self.limpiar)

        # Coloca
        self.toma_but.grid(column=2, row=7, sticky=tk.NSEW, columnspan=2)
        self.canc_but.grid(column=0, row=7, sticky=tk.NSEW, columnspan=2)

    def tomar(self):
        def separa():
            getted = self.entry_desa.get()
            try:
                getted = int(getted)
            except ValueError:
                getted = 0
            tot = getted * precios["desayuno"]

            getted = self.entry_chico.get()
            try:
                getted = int(getted)
            except ValueError:
                getted = 0
            tot += (getted * precios["chico"])

            getted = self.entry_jarrita.get()
            try:
                getted = int(getted)
            except ValueError:
                getted = 0
            tot += + (getted * precios["jarrita"])

            getted = self.entry_taza.get()
            try:
                    getted = int(getted)
            except ValueError:
                    getted = 0
            tot = tot + (getted * precios["taza"])

            getted = self.entry_doble.get()
            try:
                    getted = int(getted)
            except ValueError:
                    getted = 0
            tot = tot + (getted * precios["doble"])

            getted = self.entry_factura.get()
            try:
                    getted = int(getted)
            except ValueError:
                    getted = 0
            tot = tot + (getted * precios["factura"])

            getted = self.entry_choco.get()
            try:
                    getted = int(getted)
            except ValueError:
                    getted = 0
            tot = tot + (getted * precios["chocolatada"])

            getted = self.entry_gas.get()
            try:
                    getted = int(getted)
            except ValueError:
                    getted = 0
            tot = tot + (getted * precios["gas"])

            getted = self.entry_matete.get()
            try:
                    getted = int(getted)
            except ValueError:
                    getted = 0
            tot = tot + (getted * int(precios["matete"]))

            return tot

            # Saca mesa
            numesa = self.entry_mesa.get()
            try:
                    numesa = int(numesa)
            except ValueError:
                    numesa = 0
            self.pedido.toma_mesa(numesa)

            # Saca total
            cuenta = separa()
            self.pedido.total_msg(cuenta)

            # Crea la ventana de msg
            self.pedido.mensage()
            self.limpiar()

    def limpiar(self):
        self.entry_mesa.delete(0, 50)
        self.entry_desa.delete(0, 50)
        self.entry_chico.delete(0, 50)
        self.entry_jarrita.delete(0, 50)
        self.entry_taza.delete(0, 50)
        self.entry_doble.delete(0, 50)
        self.entry_factura.delete(0, 50)
        self.entry_choco.delete(0, 50)
        self.entry_gas.delete(0, 50)
        self.entry_matete.delete(0, 50)


class Pedido:

    def __init__(self):
        self.mesa = 0
        self.total = 0
        self.msg_mesa = "Mesa: "
        self.msg_tot = "Debe: "

    def toma_mesa(self, num):
        self.mesa = num
        self.msg_mesa = "Mesa: " + str(self.mesa)

    def total_msg(self, tot):
        self.total = tot
        self.msg_tot = "Debe: " + str(self.total)

    def mensage(self):
        self.ventana = tk.Toplevel()
        self.ventana.minsize(100, 100)
        self.ventana.title(Pedido)
        self.muestra_mesa = tk.Label(self.ventana, text=self.msg_mesa)
        self.muestra_mesa.pack()
        self.muestra_total = tk.Label(self.ventana, text=self.msg_tot)
        self.muestra_total.pack()
