import tkinter

class WelcomeFrame(tkinter.Frame):
    """Frame al ingreso"""

    def __init__(self, parent):
        """ Primer frame que se muestra """
        super().__init__(parent, bg="#FFFFFF")
        self.parent = parent
        self.label = tkinter.Label(self, text="Bienvenido")
        self.label.pack(expand=True)

