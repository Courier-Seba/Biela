"""
Root file

PLEASE READ README.md for instruccion and installation
"""

from bar_project.ui import AppRootWindow

def main():
    """Crea y ejecuta el gui del programa"""

    app = AppRootWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
