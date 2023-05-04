DROP TABLE games;
DROP TABLE users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  wins INT,
  losses INT,
  ties INT
);

CREATE TABLE games (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id),
  opponent VARCHAR(255),
  winner VARCHAR(255)
);

