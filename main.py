from Config import Config
from Feedstock import Feedstock




if __name__ == "__main__":
    config = Config()
    conn = config.get_client_sqlite()
    cursor = conn.cursor()
    with open('sql/create_tables.sql', 'rt') as f:
        schema = f.read()
        cursor.executescript(schema)

    materias = Feedstock.read(cursor)
    print(materias)

    conn.close()

