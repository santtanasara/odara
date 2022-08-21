


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
        self.table = "feedstock"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO feedstock (name, brand, quantity, measurement_unity, content) 
                VALUES (?, ?, ?, ?, ?)""", (self.name, self.brand, self.quantity, self.measurement_unity, self.content))
            self.conn.commit()
            return True
        except Exception as e:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM feedstock WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE feedstock SET name = ?, brand = ?, quantity = ?, measurement_unity = ?, content = ? 
                WHERE ID == ?""", (self.name, self.brand, self.quantity, self.measurement_unity, self.content, self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(cursor):
        try:
            cursor.execute(
                """
                SELECT * FROM feedstock;
                """
            )
            return cursor.fetchall()
        except Exception as e:
            return False