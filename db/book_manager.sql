DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    author_name VARCHAR(255),
    year_born Int,
    home_country VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    year_released INT,
    genre VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id)
);