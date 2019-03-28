import tkinter


class ClientsFrame(tkinter.Frame):
    """ Frame of Clients management """
    def __init__(self, parent):
        super().__init__(parent, bg="#0000FF")
        self.parent = parent
        self.load_widgets()

    def load_widgets(self):
        pass
