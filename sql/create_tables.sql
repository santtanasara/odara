PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS feedstock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    measurement_unity TEXT NOT NULL,
    content FLOAT NOT NULL
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
    feedstockID int,
    suplierID INT,
    price FLOAT NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date DATE NOT NULL,
    FOREIGN KEY (feedstockID) REFERENCES feedstock(id),
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

