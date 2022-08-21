class Recipies:
    def __init__(self, conn, id=None):
        self.conn = conn
        self.cursor = cursor
        self.
        self.
        self.
        self.
        self.
        self.id = id
        self.table = "Recipies"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO Recipies () 
                VALUES ?, ?, ?, ?, ?;""", ())
            self.conn.commit()
            return True
        except:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM Recipies WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE Recipies SET WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Recipies;
                """
            )
            return self.cursor.fetchall()
        except:
            return False