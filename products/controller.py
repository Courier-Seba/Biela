from bar_project.database import db_controller

# Data base controller instanse
database = db_controller


def create_product_table():
    database.create_table('Products')
    database.add_column('Products', 'prod_name', 'TEXT', required=true)
