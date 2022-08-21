

class Purchases:
    def __init__(self, conn, cursor, feedstock, suplier, price, quantity, expiration_date id=None):
        self.conn = conn
        self.cursor = cursor
        self.feedstock = feedstock
        self.suplier = suplier
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.id = id
        self.table = "Purchases"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO Purchases (id.feedstock, id.suplier, price, quantity, expiration_date) 
                VALUES ?, ?, ?, ?, ?;""", (self.feedstock, self.suplier, self.price, self.quantity, self.expiration_date))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM Purchases WHERE ID == ?;""", (self.id))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE Purchases SET WHERE ID == ?;""", (self.id))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return

    def read(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Purchases;
                """
            )
            return self.cursor.fetchall()
        except:
            return False
