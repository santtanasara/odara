class Product:
    def __init__(self, conn, cursor, recipieID, price, creation_date, quantity, id=None):
        self.conn = conn
        self.cursor = cursor
        self.recipieID = recipieID
        self.price = price
        self.creation_date = creation_date
        self.quantity = quantity
        self.id = id
        self.table = "products"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO products (recipieID, price, creation_date, quantity) 
                VALUES (?, ?, ?, ?)""", (self.recipieID, self.price, self.creation_date, self.quantity))
            self.conn.commit()
            return True
        except Exception as e:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM products WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE products SET recipieID = ?, price = ?, creation_date = ?, quantity = ? 
                WHERE ID == ?;""", (self.recipieID, self.price, self.creation_date, self.quantity, self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(cursor):
        try:
            cursor.execute(
                """
                SELECT * FROM products;
                """
            )
            return cursor.fetchall()
        except Exception as e:
            return False