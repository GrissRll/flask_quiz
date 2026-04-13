import sqlite3


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("new_db")
        self.cursor = self.conn.cursor()

    def insert_data(self, query, data=None, flag=True):
        data = data if data else []
        self.conn = sqlite3.connect("new_db")
        if flag:
            self.cursor.execute(query, data)
        else:
            self.cursor.executemany(query, data)
        self.conn.commit()
        self.conn.close()

    def get_data(self, query, data=None):
        data = data if data else []
        self.conn = sqlite3.connect("new_db")
        self.cursor.execute(query, data)
        db_data = self.cursor.fetchall()
        return db_data

    def exc_script(self, script):
        self.conn = sqlite3.connect("new_db")
        self.cursor.executescript(script)
        self.conn.commit()
        self.conn.close()