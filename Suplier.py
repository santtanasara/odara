class Suplier:
    def __init__(self, conn,cursor, name, website, id=None):
        self.conn = conn
        self.cursor = cursor
        self.name = name
        self.website = website
        self.id = id
        self.table = "Suplier"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO Suplier (name, website, id) 
                VALUES ?, ?, ?, ?, ?;""", (self.name, self.website, self.id))
            self.conn.commit()
            return True
        except:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM Suplier WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE Suplier SET WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(self):
        try:
            self.cursor.execute(
                """
                SELECT * FROM Suplier;
                """
            )
            return self.cursor.fetchall()
        except:
            return False