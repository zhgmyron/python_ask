drop TABLE if exists entries;

CREATE TABLE entries(
  id INTEGER PRIMARY KEY autoincrement,
  title text not NULL,
  text text not NULL
)