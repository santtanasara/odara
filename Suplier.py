class Suplier:
    def __init__(self, conn,cursor, name, website, id=None):
        self.conn = conn
        self.cursor = cursor
        self.name = name
        self.website = website
        self.id = id
        self.table = "supliers"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO supliers (name, website) 
                VALUES (?, ?)""", (self.name, self.website))
            self.conn.commit()
            return True
        except Exception as e:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM supliers WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE supliers SET name = ?, website = ?
                WHERE ID == ?;""", (self.name, self.website, self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(cursor):
        try:
            cursor.execute(
                """
                SELECT * FROM supliers;
                """
            )
            return cursor.fetchall()
        except:
            return False