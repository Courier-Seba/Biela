import tkinter

class TitleLabel(tkinter.Label):
        """ Title of Frame """

        def __init__(self, master, text):
                super().__init__(master, text=text, bg="#FF0000")


class AddButton(tkinter.Button):
    """ Button for adding 1 product"""

    def __init__(master, texto):
        super().__init__(
            master,
            text=texto,
        )


class InsertProductsEntry(tkinter.Entry):
        """ Entry for inserting products """

        def __init__(self, master):
            super().__init__(master, bg="#FFFFFF", fg="#000000")
            self.insert(0, "0")

        def add_one(self):
            cantActual = self.toma_dato()
            cantFinal = cantActual + 1
            self.delete(0, tkinter.END)
            self.insert(0, str(cantFinal))

        def read(self):
            data = self.get()
            try:
                dataInt = int(dato)
            except:
                ValueError: print("U miss")
            return datoInt

class TextLabel(tkinter.Label):
    """ Label for display text """

    def __init__(self, master, text):
        super().__init__(
            master,
            bg="#FFFFFF",
            fg="#000000",
            text=text
        )

class LargeButton(tkinter.Button):
    """ Large button that fills x """

        # TODO: Falta el controller
    def __init__(self, master, texto, **kwargs):
        super().__init__(
            master,
            text=texto,
            bg="#FFFFFF",
            fg="#000000",
            command=lambda: self.ejecuta()
            )
        self.master = master
        self.kw = kwargs


    def ejecuta(self):
        for key, value in self.kw.items():
            if (key == "operacion"):
                return getattr(self.master, value)()
            else:
                return ""

class BoxedLabel(tkinter.Label):
    """ Label with Border """

    def __init__(self, master, contenido):
        super().__init__(
            master,
            text=contenido,
            fg="#000000",
            bd=10,
            bg="#FFFFFF"
        )
