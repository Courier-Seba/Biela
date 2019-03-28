import tkinter
from bar_project.widgets.app_wide import TitleLabel, InsertEntry, LargeButton
from gestion import productos



class OrderFrame(tkinter.Frame):
    """Frame de ingreso"""

    def __init__(self, parent):
        super().__init__(parent, bg="#FFFFFF")
        self.parent = parent
        self.load_widgets()

    def load_widgets(self):
        """ Load all widgets """
        pass
