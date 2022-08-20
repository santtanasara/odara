


class Feedstock:
    def __init__(self, conn, cursor, name, brand, quantity, measurement_unity, content, id=None):
        self.conn = conn
        self.cursor = cursor
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.measurement_unity = measurement_unity
        self.content = content
        self.id = id
        self.table = "Feedstock"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO Feedstock (name, brand, quantity, measurement_unity, content) 
                VALUES ?, ?, ?, ?, ?;""", (self.name, self.brand, self.quantity, self.measurement_unity, self.content))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM Feedstock WHERE ID == ?;""", (self.id))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE Feedstock SET WHERE ID == ?;""", (self.id))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return

    def read(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Feedstock;
                """
            )
            return self.cursor.fetchall()
        except:
            return False