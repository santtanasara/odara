from Config import Config


class Feedstock:
    def __init__(self, name, brand, measurement_unity, quantity, content, id_purchase, category, id=None):
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.measurement_unity = measurement_unity
        self.content = content
        self.id_purchase = id_purchase
        self.id = id
        self.table = "feedstock"
        self.category = category

    def create(self):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """INSERT INTO feedstock (name, brand, measurement_unity, quantity, content, category, id_purchase) 
                VALUES (?, ?, ?, ?, ?, ?, ?)""", (self.name, self.brand, self.measurement_unity, self.quantity,
                                               self.content, self.category, self.id_purchase))
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
                """DELETE FROM feedstock WHERE ID == ?;""", (self.id))
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
                """UPDATE feedstock SET name = ?, brand = ?, measurement_unity = ?, quantity = ?, content = ?, 
                category = ?, id_purchase = ? 
                WHERE ID == ?""", (self.name, self.brand, self.measurement_unity, self.quantity,
                                   self.content, self.id_purchase, self.id))
            conn.commit()
            config.disconnect_sqlite()
            return True
        except:
            return

    @staticmethod
    def read(category=None, id=None):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            if not id and not category:
                cursor.execute(
                    """
                    SELECT * FROM feedstock;
                    """
                )
            elif id and not category:
                cursor.execute(
                    """
                    SELECT * FROM feedstock WHERE id == ?;
                    """, id)

            elif category:
                cursor.execute(
                    """
                    SELECT id, name, brand, measurement_unity, sum(quantity) AS quantity, 
                    sum(content) AS content, category  
                    FROM feedstock WHERE category == ?
                    GROUP BY name;
                    """, (category, )
                )
            result = cursor.fetchall()
            config.disconnect_sqlite()
            return result
        except Exception as e:
            return False

    @staticmethod
    def read_last_register():
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """
                SELECT * FROM feedstock ORDER BY id desc LIMIT 1;
                """
            )
            result = cursor.fetchone()
            config.disconnect_sqlite()
            return result
        except:
            return False

    @staticmethod
    def read_by_name(name):
        try:
            config = Config()
            conn, cursor = config.get_client_sqlite()
            cursor.execute(
                """
                SELECT * FROM feedstock WHERE name == ? ORDER BY id asc;
                """, name
            )
            result = cursor.fetchone()
            config.disconnect_sqlite()
            return result
        except:
            return False
