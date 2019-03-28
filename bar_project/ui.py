""" Base zone """
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
        for frame in frames.frames:
            page_name = frame.__name__
            new_frame = frame(parent=self.container)
            self.frames_container[page_name] = new_frame
            new_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Carga el primero
        self.load_frame("WelcomeFrame")

    def load_frame(self, page_name):
        """ Loads a frame """
        for frame in self.frames_container.values():
            frame.place_forget()
        frame = self.frames_container[page_name]
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


class AppRootWindow(tkinter.Tk):
    """ Root app """

    def __init__(self):
        super().__init__()
        # Configuracion de la ventana principal
        # Titulo ventana
        self.title(settings.title)

        self.minsize(settings.minsize["x"], settings.minsize["y"])
        # FOR my I3 tilling wm
        if settings.debug:
            self.attributes('-type', 'dialog')

        # Main Frame
        self.main_frame = Main(self)
        self.main_frame.pack(expand=False, fill=tkinter.BOTH)

        # Menu bar
        if settings.display_menu:
            self.menu_bar = MenuBar(self, self.main_frame)
            self.config(menu=self.menu_bar)
