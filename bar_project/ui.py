# Python import
import tkinter

# Settings
from . import settings
from .frames import frames

class Main(tkinter.Frame):
    """Frame mas bajo, sobre el se crean los demas"""
    def __init__(self, parent):
        super().__init__(parent, bg="#FFFFFF")
        self.parent = parent

        # Container de los frames que cambian
        self.container = tkinter.Frame()
        self.container.pack(side=tkinter.RIGHT, expand=True)
        self.frames_container = {}

        # Crea cada frame
        for Frame in frames:
            page_name = Frame.__name__
            frame_creado = Frame(parent=self.container)
            self.frames_container[page_name] = frame_creado
            frame_creado.grid(row=0, column=0, sticky=tkinter.NSEW)
        # Carga el primero
        self.carga_frame("WelcomeFrame")

    def carga_frame(self, page_name):
        """ Carga el frame dado"""
        frame = self.frames_container[page_name]
        frame.tkraise()

class AppRootWindow(tkinter.Tk):
    """Root app"""

    def __init__(self, *args, **kwargs):
        super().__init__()
        # Configuracion de la ventana principal
        # Titulo ventana
        self.title(settings.title)

        # Size
        self.configure(background=settings.background)

        # Main Frame
        self.mainFrame = Main(self)
        self.mainFrame.pack()
