from Config import Config
from interfaces import main





if __name__ == "__main__":
    config = Config()
    conn, cursor = config.get_client_sqlite()
    with open('sql/create_tables.sql', 'rt') as f:
        schema = f.read()
        cursor.executescript(schema)

    main.run()
    config.disconnect_sqlite()

