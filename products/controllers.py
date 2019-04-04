""" Product Cotroller
This manage the products db
"""


class Product:
    """ Product class """

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.state = True

