import sqlite3

def connect(func):
	def wrapper_connect():
		conn = sqlite3.connect("library_database.db")
		cur = conn.cursor()
		func(cur,conn)
		conn.close()
	return wrapper_connect

@connect
def create_table(cursor, connection):
	cursor.execute("CREATE TABLE if not EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, year_read INTEGER)")
	connection.commit()

create_table()