from Config import Config

class Recipies:
    def __init__(self, name, weight, category, feedstock, id=None):
        self.name = name
        self.weight = weight
        self.category = category
        self.feedstock = feedstock
        self.id = id
        self.table = "recipies"

    def create(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """INSERT INTO recipies (name, weight, category, feedstock) 
                VALUES (?, ?, ?, ?)""", (self.name, self.weight, self.category, self.feedstock))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    def delete(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """DELETE FROM recipies WHERE ID == ?;""", (self.id))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    def update(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """UPDATE recipies SET name = ?, weight = ?, category = ?, feedstock = ?
                 WHERE ID == ?;""", (self.name, self.weight, self.category, self.id))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    @staticmethod
    def read(id=None):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            if not id:
                cursor.execute(
                    """
                    SELECT * FROM recipies;
                    """
                )
                result = cursor.fetchall()
            else:
                cursor.execute(
                    """
                    SELECT * FROM recipies WHERE id == ?;
                    """, id
                )
                result = cursor.fetchone()
            config.disconnect_sqlite()
            return result
        except:
            return False