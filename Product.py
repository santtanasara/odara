class Product:
    def __init__(self, conn, id=None):
        self.conn = conn
        self.cursor = cursor
        self.
        self.
        self.
        self.
        self.
        self.id = id
        self.table = "Product"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO Product () 
                VALUES ?, ?, ?, ?, ?;""", ())
            self.conn.commit()
            return True
        except:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM Product WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE Product SET WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Product;
                """
            )
            return self.cursor.fetchall()
        except:
            return False