-- Create Cuisine table
CREATE TABLE Cuisine (
    id SERIAL PRIMARY KEY, 
    name VARCHAR NOT NULL
);

-- Insert into Cuisine
INSERT INTO Cuisine (name)
VALUES 
    ('Goodfella chicken platters'),
    ('Wise guy special (Pizza dishes)'), 
    ('Sleeping with the fishes (Fish themed meals)'),
    ('Don''t know nothing meals (Other non main course meals -- Appetizers and desserts)');

-- Create Category table
CREATE TABLE Category (
    id SERIAL PRIMARY KEY, 
    name VARCHAR NOT NULL
);

-- Insert into Category
INSERT INTO Category (name)
VALUES 
    ('Breakfast'),
    ('Lunch'),
    ('Dinner');

-- Create MenuItems table
CREATE TABLE MenuItems (
    id SERIAL PRIMARY KEY, 
    title VARCHAR, 
    description TEXT, 
    price FLOAT, 
    spiciness INT,
    category_id INTEGER REFERENCES Category(id),
    cuisine_id INTEGER REFERENCES Cuisine(id),

    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
        REFERENCES Category(id),
    
    CONSTRAINT fk_cuisine
        FOREIGN KEY (cuisine_id)
        REFERENCES Cuisine(id)
);


