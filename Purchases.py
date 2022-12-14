from Feedstock import Feedstock
from Config import Config
from datetime import datetime
import sqlite3

class Purchases:
    def __init__(self, feedstock, suplier, price, quantity, unity_price, expiration_date, category, id=None):
        self.feedstock = feedstock
        self.suplier = suplier
        self.price = price
        self.quantity = quantity
        self.unity_price = unity_price
        self.expiration_date = expiration_date
        self.id = id
        self.table = "purchases"
        self.category = category

    def create(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """INSERT INTO purchases (suplierID, price, unity_price, quantity, category, expiration_date, buying_date) 
                VALUES (?, ?, ?, ?, ?, ?, ?)""", (self.suplier, self.price, self.unity_price, self.quantity, self.category,
                                         self.expiration_date, datetime.now()))
            conn.commit()

            id_last_register = self.read_last_register()[0]
            for i in range(0, self.quantity):
                new_feedstock = Feedstock(self.feedstock["name"], self.feedstock["brand"],
                                          self.feedstock["measurement_unity"], 1,
                                          self.feedstock["content"], id_last_register, self.category)
                new_feedstock.create()

            config.disconnect_sqlite()
            return True
        except Exception as e:
            return

    def delete(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """DELETE FROM purchases WHERE ID == ?;""", (self.id))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    def update(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """UPDATE purchases SET suplier = ?, price = ?, unity_price = ?, quantity = ?, 
                category = ?, expiration_date = ?
                WHERE id == ?;""", (self.suplier, self.price, self.unity_price,
                                    self.quantity, self.category, self.expiration_date, self.id))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    @staticmethod
    def read(category):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            conn.row_factory = sqlite3.Row
            cursor.execute(
                """
                SELECT s.name, f.name as f_name, f.brand, f.measurement_unity, f.content, p.price, p.unity_price, p.quantity, p.expiration_date, p.buying_date
                 FROM purchases as p 
                 JOIN supliers as s ON p.id == s.id 
                 JOIN feedstock as f ON f.id == p.id WHERE p.category == ?
                """, (category, )
            )
            rows =  cursor.fetchall()
            columns = cursor.description
            config.disconnect_sqlite()
            return rows, [col[0] for col in columns]
        except Exception as e:
            return False

    def read_last_register(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """
                SELECT * FROM purchases ORDER BY id desc LIMIT 1;
                """
            )
            result = cursor.fetchone()
            config.disconnect_sqlite()
            return result
        except:
            return False
