import sqlite3


class DataBase:
    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def insert_data(self, query, data=None, flag=True):
        self.conn = sqlite3.connect(self.DATABASE)
        self.cursor = self.conn.cursor()
        data = data if data else []

        if flag:
            self.cursor.execute(query, data)
        else:
            self.cursor.executemany(query, data)
        self.conn.commit()
        self.conn.close()

    def get_data(self, query, data=None):
        self.conn = sqlite3.connect(self.DATABASE)
        self.cursor = self.conn.cursor()
        data = data if data else []
        self.cursor.execute(query, data)
        db_data = self.cursor.fetchall()
        return db_data

    def exc_script(self, script):
        self.conn = sqlite3.connect(self.DATABASE)
        self.cursor = self.conn.cursor()
        self.cursor.executescript(script)
        self.conn.commit()
        self.conn.close()