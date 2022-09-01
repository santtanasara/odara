PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS feedstock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    measurement_unity TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    content FLOAT NOT NULL,
    category TEXT,
    id_purchase INT,
    FOREIGN KEY (id_purchase) REFERENCES purchases(id)
    FOREIGN KEY (category) REFERENCES category(name)
);

CREATE TABLE IF NOT EXISTS supliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    website TEXT
);

CREATE TABLE IF NOT EXISTS recipies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    weight FLOAT NOT NULL,
    category TEXT,
    feedstock TEXT NOT NULL

);

CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    suplierID INT,
    price FLOAT NOT NULL,
    unity_price FLOAT NOT NULL,
    quantity INTEGER NOT NULL,
    category TEXT,
    expiration_date DATE,
    buying_date DATE NOT NULL,
    FOREIGN KEY (suplierID) REFERENCES supliers(id)
    FOREIGN KEY (category) REFERENCES category(name)
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipieID INT,
    price FLOAT,
    creation_date DATE NOT NULL,
    quantity INT,
    FOREIGN KEY (recipieID) REFERENCES recipies(id)

);

CREATE TABLE IF NOT EXISTS category (
    name TEXT PRIMARY KEY
)

