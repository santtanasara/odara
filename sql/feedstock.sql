CREATE TABLE IF NOT EXISTS feedstock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    measurement_unity TEXT NOT NULL,
    content FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedstockID int,
    price FLOAT NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date DATE NOT NULL,
    FOREIGN KEY (feedstockID) REFERENCES feedstock(id)

);

CREATE TABLE IF NOT EXISTS suplier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    website TEXT NOT NULL
);

