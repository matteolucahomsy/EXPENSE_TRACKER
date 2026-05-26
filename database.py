import sqlite3

conn = sqlite3.connect("expenses.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               amount REAL,
               category Text,
               date TEXT,
               user_id INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE,
               password TEXT
               );
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS budget(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               amount REAL,
               user_id INTEGER UNIQUE
               );
""")
conn.commit()
conn.close()