import sqlite3

conn = sqlite3.connect("expenses.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               amount REAL,
               category Text,
               date TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE,
               password TEXT
               );
""")

conn.commit()
conn.close()