import tkinter

class StatsFrame(tkinter.Frame):
    """ Frame to show stadistics of sales """

    def __init__(self, parent):
        super().__init__(parent, bg="#0000FF")
        self.parent = parent
        self.load_widgets()

    def load_widgets(self):
        """ Load widgets """
        pass
