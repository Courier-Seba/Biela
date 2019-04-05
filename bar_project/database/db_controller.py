import os
import sqlite3


DB_FOLDER_PATH = os.getcwd()
DB_PATH = DB_FOLDER_PATH + "/db.sqlite3"


if __name__ == "__main__":
    connection = sqlite3.connect(DB_PATH)
    connection.close()
