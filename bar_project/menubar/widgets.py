import tkinter


class MenuBar(tkinter.Menu):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.parent = parent
        self.controller = controller

        self.file_menu = FileMenu(self)
        self.add_cascade(label="File", menu=self.file_menu)

        self.products_menu = ProductsMenu(self, self.controller)
        self.add_cascade(
            label="Products",
            menu=self.products_menu,
        )


class FileMenu(tkinter.Menu):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.add_command(label="Exit", command=lambda: quit())

class ProductsMenu(tkinter.Menu):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        self.add_command(
            label="New Product",
            command=lambda: controller.load_frame("NewProductFrame")
        )

        self.add_command(
            label="List of Products",
            underline=0,
            command=lambda: controller.load_frame("ListProductsFrame")
        )
