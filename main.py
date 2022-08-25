from Config import Config






if __name__ == "__main__":
    config = Config()
    conn, cursor = config.get_client_sqlite()
    with open('sql/create_tables.sql', 'rt') as f:
        schema = f.read()
        cursor.executescript(schema)

    cursor.execute("SELECT * FROM recipies;")
    print(cursor.fetchall())

    config.disconnect_sqlite()

