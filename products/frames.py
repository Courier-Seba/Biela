""" Product module frames """

import tkinter

from .config import Config
from gestion import productos

from bar_project.widgets.app_wide import TitleLabel, InsertEntry, TextLabel, \
    LargeButton, BoxedLabel

class NewProductFrame(tkinter.Frame):
    """ Frame for adding products """

    def __init__(self, parent):
        super().__init__(parent, bg="#FFFFFF")
        self.parent = parent
        self.load_widgets()


    def load_widgets(self):
        """ Load Frame widgets """

        self.title = TitleLabel(self, Config.FRAME_TITLE)
        self.new_product_label = TextLabel(self, Config.NEW_PR_LABEL_NAME)
        self.new_desc_label = TextLabel(self, Config.NEW_PR_LABEL_DESC)
        self.new_value_label = TextLabel(self, Config.NEW_PR_LABEL_PRICE)
        self.new_product_entry = InsertEntry(self)
        self.new_desc_entry = InsertEntry(self)
        self.new_value_entry = InsertEntry(self)
        self.cancel_button = LargeButton(
            self,
            "Cancel",
            self.get_product
        )
        self.take_button = LargeButton(
            self,
            "Add",
            self.get_product
        )

        self.title.grid(column=0, row=0, columnspan=99)
        self.new_product_label.grid(column=0, row=2)
        self.new_product_entry.grid(column=1, row=2)
        self.new_desc_label.grid(column=0, row=3)
        self.new_desc_entry.grid(column=1, row=3)
        self.new_value_label.grid(column=0, row=4)
        self.new_value_entry.grid(column=1, row=4)
        self.cancel_button.grid(column=0, row=5, sticky=tkinter.NSEW)
        self.take_button.grid(column=1, row=5, sticky=tkinter.NSEW)

    def get_product(self):
        """ Return list with the data """
        data_input = []
        data_input.append(self.new_product_entry.read())
        data_input.append(self.new_desc_entry.read())
        data_input.append(self.new_value_entry.read())

        return data_input



class ListProductsFrame(tkinter.Frame):
    """ List of all products """

    def __init__(self, parent):
        super().__init__(parent)
        self.load_widgets()

    def load_widgets(self):
        """ To load/reload widgets """
        self.title = TitleLabel(self, "Products List")
        self.title.grid(column=0, row=0)

