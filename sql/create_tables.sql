PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS feedstock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    measurement_unity TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    content FLOAT NOT NULL,
    id_purchase INT,
    FOREIGN KEY (id_purchase) REFERENCES purchases(id)
);

CREATE TABLE IF NOT EXISTS supliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    website TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS recipies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    weight FLOAT NOT NULL,
    category TEXT NOT NULL,
    feedstock TEXT NOT NULL

);

CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    suplierID INT,
    price FLOAT NOT NULL,
    unity_price FLOAT NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date DATE NOT NULL,
    FOREIGN KEY (suplierID) REFERENCES supliers(id)
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipieID INT,
    price FLOAT NOT NULL,
    creation_date DATE NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (recipieID) REFERENCES recipies(id)

);

