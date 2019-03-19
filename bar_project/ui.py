# Python import
import tkinter

# Settings
from . import settings
from .menubar.widgets import MenuBar

# Frames
from . import frames

class Main(tkinter.Frame):
    """ Frame mas bajo, sobre el se crean los demas """
    def __init__(self, parent):
        super().__init__(parent, bg=settings.app_bg)
        self.parent = parent

        # Container de frames que cambian
        self.container = tkinter.Frame()
        self.container.pack(expand=True, fill=tkinter.BOTH)
        self.frames_container = {}

        # Crea cada frame
        for Frame in frames.frames:
            page_name = Frame.__name__
            new_frame = Frame(parent=self.container)
            self.frames_container[page_name] = new_frame
            new_frame.grid(row=0, column=0, sticky=tkinter.NSEW)

        # Carga el primero
        self.load_frame("WelcomeFrame")

    def load_frame(self, page_name):
        """ Loads a frame """
        frame = self.frames_container[page_name]
        frame.tkraise()

class AppRootWindow(tkinter.Tk):
    """ Root app """

    def __init__(self, *args, **kwargs):
        super().__init__()
        # Configuracion de la ventana principal
        # Titulo ventana
        self.title(settings.title)

        # Main Frame
        self.main_frame = Main(self)
        self.main_frame.pack(expand=True, fill=tkinter.BOTH)

        # Menu
        if settings.display_menu:
            self.menu_bar = MenuBar(self, self.main_frame)
            self.config(menu=self.menu_bar)
