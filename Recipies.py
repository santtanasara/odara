class Recipies:
    def __init__(self, conn, cursor, name, weight, category, feedstock, id=None):
        self.conn = conn
        self.cursor = cursor
        self.name = name
        self.weight = weight
        self.category = category
        self.feedstock = feedstock
        self.id = id
        self.table = "recipies"

    def create(self):
        try:
            self.cursor.execute(
                """INSERT INTO recipies (name, weight, category, feedstock) 
                VALUES (?, ?, ?, ?)""", (self.name, self.weight, self.category, self.feedstock))
            self.conn.commit()
            return True
        except:
            return

    def delete(self):
        try:
            self.cursor.execute(
                """DELETE FROM recipies WHERE ID == ?;""", (self.id))
            self.conn.commit()
            return True
        except:
            return

    def update(self):
        try:
            self.cursor.execute(
                """UPDATE recipies SET name = ?, weight = ?, category = ?, feedstock = ?
                 WHERE ID == ?;""", (self.name, self.weight, self.category, self.id))
            self.conn.commit()
            return True
        except:
            return

    @staticmethod
    def read(cursor):
        try:
            cursor.execute(
                """
                SELECT * FROM recipies;
                """
            )
            return cursor.fetchall()
        except:
            return False