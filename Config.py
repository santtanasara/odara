import sqlite3

class Config:
    def __init__(self):
        self.sqlite_client = sqlite3.connect("odara")

    def get_client_sqlite(self):
        return self.sqlite_client, self.sqlite_client.cursor()

    def disconnect_sqlite(self):
        self.sqlite_client.close()

