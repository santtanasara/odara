from Config import Config
from Recipies import Recipies
from Feedstock import Feedstock

class Product:
    def __init__(self, recipieID, price, creation_date, quantity, id=None):
        self.recipieID = recipieID
        self.price = price
        self.creation_date = creation_date
        self.quantity = quantity
        self.id = id
        self.table = "products"

    def create(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """INSERT INTO products (recipieID, price, creation_date, quantity) 
                VALUES (?, ?, ?, ?)""", (self.recipieID, self.price, self.creation_date, self.quantity))

            recipie = Recipies.read(id=self.recipieID)
            for k, v in recipie[-1].items(): #transformar em dict
                feedstock = Feedstock.read_by_name(k)
                change_next_feedstock = False
                for i in range(0, feedstock):
                    content_diference = feedstock[i][4] - abs(v)
                    if content_diference > 0:
                        change_next_feedstock = False
                    else:
                        change_next_feedstock = True
                    feedstock_update = Feedstock(feedstock[i][1], feedstock[i][2], feedstock[i][3],
                                                 feedstock[i][4] if not change_next_feedstock else 0,
                                                 content_diference if not change_next_feedstock else 0,
                                                 feedstock[i][6], feedstock[i][0])
                    feedstock_update.update()
                    if not change_next_feedstock:
                        break
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
                """DELETE FROM products WHERE ID == ?;""", (self.id))
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
                """UPDATE products SET recipieID = ?, price = ?, creation_date = ?, quantity = ? 
                WHERE ID == ?;""", (self.recipieID, self.price, self.creation_date, self.quantity, self.id))
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
                SELECT * FROM products;
                """
            )
            result =  cursor.fetchall()
            config.disconnect_sqlite()
            return result
        except Exception as e:
            return False