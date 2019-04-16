"""
All the database api operations are here, including app specific.
"""

from db_controller import Database

def create_product_table():
    db = Database()
    db.create_table('Product')
    db.close_connection()

if __name__ == "__main__":
    create_product_table()
