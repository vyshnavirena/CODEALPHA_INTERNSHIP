import sqlite3

connection = sqlite3.connect("users.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

connection.commit()
connection.close()

print("Database created successfully!")