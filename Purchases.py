

class Purchases:
    def __init__(self, conn, cursor, feedstock, suplier, price, quantity, expiration_date, id=None):
        self.conn = conn
        self.cursor = cursor
        self.feedstock = feedstock
        self.suplier = suplier
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.id = id
        self.table = "purchases"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO purchases (feedstockID, suplierID, price, quantity, expiration_date) 
                VALUES (?, ?, ?, ?, ?)""", (self.feedstock, self.suplier, self.price, self.quantity, self.expiration_date))
            self.conn.commit()
            return True
        except Exception as e:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM purchases WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE purchases SET feedstock = ?, suplier = ?, price = ?, quantity = ?, expiration_date = ?
                WHERE ID == ?;""", (self.feedstock, self.suplier, self.price, self.quantity, self.expiration_date, self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(cursor):
        try:
            cursor.execute(
                """
                SELECT * FROM purchases;
                """
            )
            return cursor.fetchall()
        except Exception as e:
            return False
