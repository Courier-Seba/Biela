import os
import sqlite3



class Database:
    """ Here lies the whole db controller

    """
    DB_FOLDER_PATH = os.getcwd()
    DB_PATH = DB_FOLDER_PATH + "/db.sqlite3"

    def __init__(self):
        self.create_connection()
        self.get_cursor()

    def create_connection(self):
        """
        Starts a connection to the DB
        """
        self.connection = sqlite3.connect(self.DB_PATH)

    def get_cursor(self):
        """ Sets the cursor first time """
        self.cursor = self.connection.cursor()

    def close_connection(self):
        """
        Close connection
        """
        self.connection.close()


    def create_table(self, table_name):
        """ create a new table and set id column"""
        pk_column_name = table_name + '_id'
        self.cursor.execute(
            'CREATE TABLE {tn} ( {pk} INTEGER PRIMARY KEY)'\
            .format(tn=table_name,  pk=pk_column_name)
        )
        self.connection.commit()
        return print("New table created")

    def add_column(self, table_name, column_name, column_type, **kwargs):
        """ Add a column to a table in the db """
        self.cursor.execute(
            'ALTER TABLE {tn} ADD COLUMN {cn} {ct}'\
            .format(tn=table_name, cn=column_name, ct=column_type)
        )

