from Feedstock import Feedstock
from Config import Config

class Purchases:
    def __init__(self, feedstock, suplier, price, quantity, unity_price, expiration_date, id=None):
        self.feedstock = feedstock
        self.suplier = suplier
        self.price = price
        self.quantity = quantity
        self.unity_price = unity_price
        self.expiration_date = expiration_date
        self.id = id
        self.table = "purchases"

    def create(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """INSERT INTO purchases (suplierID, price, unity_price, quantity, expiration_date) 
                VALUES (?, ?, ?, ?, ?)""", (self.suplier, self.price, self.unity_price, self.quantity,
                                         self.expiration_date))

            id_last_register = self.read_last_register()[0]
            for i in range(0, self.feedstock["quantity"]):
                new_feedstock = Feedstock(self.feedstock["name"], self.feedstock["brand"],
                                          i+1, self.feedstock["measurement_unity"], 1,
                                          self.feedstock["content"], id_last_register)
                new_feedstock.create()

                conn.commit()
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
                """UPDATE purchases SET suplier = ?, price = ?, unity_price = ?, quantity = ?, expiration_date = ?
                WHERE id == ?;""", (self.suplier, self.price, self.unity_price,
                                    self.quantity, self.expiration_date, self.id))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    @staticmethod
    def read():
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """
                SELECT * FROM purchases;
                """
            )
            result =  cursor.fetchall()
            config.disconnect_sqlite()
            return result
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
