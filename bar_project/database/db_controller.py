import os
import sqlite3



class Database:
    """ Here lies the whole db controller

    """
    DB_FOLDER_PATH = os.getcwd()
    DB_PATH = DB_FOLDER_PATH + "/db.sqlite3"

    def __init__(self):
        self._connection
        self._cursor

    def _create_connection(self):
        """
        Starts a connection to the DB
        """
        self._connection = sqlite3.connect(DB_PATH)

    def _close_connection(self):
        """
        Close connection
        """
        self._connection.close()

    def _get_cursor(self):
        self._connection

    def create_table(self):


if __name__ == "__main__":
    conn = create_connection()
    close_connection(conn)
