# Python import
import tkinter

# Settings
from . import settings
from . import frames

############################ MAIN FRAME #######################################
class Main(tkinter.Frame):
    """Frame mas bajo, sobre el se crean los demas"""
    def __init__(self, parent):
        super().__init__(parent, bg=settings.app_bg)
        self.parent = parent

        # Container de frames que cambian
        self.container = tkinter.Frame()
        self.container.pack(expand=True)
        self.frames_container = {}

        # Crea cada frame
        for Frame in frames.frames:
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

###############################################################################

class MenuBar(tkinter.Menu):

    def __init__(self, parent):
        super().__init__(parent)

        self.file_menu = tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=self.file_menu)
        self.file_menu.add_command(label="Exit", underline=0, command=lambda: quit())

class AppRootWindow(tkinter.Tk):
    """Root app"""

    def __init__(self, *args, **kwargs):
        super().__init__()
        # Configuracion de la ventana principal
        # Titulo ventana
        self.title(settings.title)

        # Main Frame
        self.main_frame = Main(self)
        self.main_frame.pack()

        # Menu
        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)
