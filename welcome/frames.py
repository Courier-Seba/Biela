import tkinter

from .config import Config


class WelcomeFrame(tkinter.Frame):
    """ First frame to start """

    def __init__(self, parent):
        super().__init__(parent, bg=Config.BG)
        self.parent = parent

        self.label = tkinter.Label(self, text=Config.INTRO_TEXT)
        self.label.pack(expand=True)

