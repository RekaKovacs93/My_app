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
  name VARCHAR(255)
);

-- CREATE TABLE visits (
--   id SERIAL PRIMARY KEY,
--   user_id INT REFERENCES users(id) ON DELETE CASCADE,
--   location_id INT NOT NULL REFERENCES locations(id) ON DELETE CASCADE,
--   review TEXT
-- );
