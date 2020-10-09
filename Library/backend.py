import sqlite3

conn = sqlite3.connect("library_database.db")
cur = conn.cursor()
cur.execute("CREATE TABLE if not EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, year_read INTEGER)")
conn.commit()
conn.close()