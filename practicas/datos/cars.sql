DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    model TEXT,
    engine TEXT,
    capacity INTEGER,
    horsepower INTEGER,
    top_speed INTEGER,
    acceleration REAL,
    price INTEGER,
    fuel_type TEXT,
    seats INTEGER,
    torque TEXT
);