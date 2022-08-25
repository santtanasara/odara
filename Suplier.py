from Config import Config

class Suplier:
    def __init__(self, name, website, id=None):
        self.name = name
        self.website = website
        self.id = id
        self.table = "supliers"

    def create(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """INSERT INTO supliers (name, website) 
                VALUES (?, ?)""", (self.name, self.website))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except Exception as e:
            return

    def delete(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """DELETE FROM supliers WHERE ID == ?;""", (self.id))
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
                """UPDATE supliers SET name = ?, website = ?
                WHERE ID == ?;""", (self.name, self.website, self.id))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    @staticmethod
    def read():
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """
                SELECT * FROM supliers;
                """
            )
            result =  cursor.fetchall()
            config.disconnect_sqlite()
            return result
        except:
            return False