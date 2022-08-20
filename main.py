from Config import Config




if __name__ == "__main__":
    config = Config()
    sqlite_client = config.get_client_sqlite()

