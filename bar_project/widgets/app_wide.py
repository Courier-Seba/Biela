"""
    Global Creation of widgets
    From here change, style or add widgtes easily

    TODO: Send colors to settings
"""
import tkinter

class TitleLabel(tkinter.Label):
    """ Title of Frame """

    def __init__(self, master, text):
        super().__init__(master, text=text, bg="#FF0000")


class InsertEntry(tkinter.Entry):
    """ Entry for inserting data """

    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF", fg="#000000")
        self.insert(0, "0")

    def read(self):
        """ Return the input at the moment """

        data = self.get()
        return data

class TextLabel(tkinter.Label):
    """ Label for display text """

    def __init__(self, master):
        self.text = ""

        # Call the constructor of tk
        super().__init__(
            master,
            bg="#FFFFFF",
            fg="#000000",
            text=self.text
        )

class LargeButton(tkinter.Button):
    """ Large button that fills x """

    def __init__(self, master, texto, controller):
        super().__init__(
            master,
            text=texto,
            bg="#FFFFFF",
            fg="#000000",
            command=controller
        )
        self.master = master


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
