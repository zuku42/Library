import sqlite3

def connect(func):
	def wrapper_connect(*args, **kwargs):
		conn = sqlite3.connect("library_database.db")
		cur = conn.cursor()
		returned_value = func(cur, conn, *args, **kwargs)
		conn.close()
		return returned_value
	return wrapper_connect

@connect
def create_table(cursor, connection):
	cursor.execute("CREATE TABLE if not EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, year_read INTEGER)")
	connection.commit()

@connect
def view(cursor, connection):
	cursor.execute("SELECT * FROM books")
	rows = cursor.fetchall()
	return rows

@connect
def search(cursor, connection, title="", author="", year="", year_read=""):
	cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR year_read=?",(title, author, year, year_read))
	rows = cursor.fetchall()
	return rows

@connect
def insert(cursor, connection, title, author, year, year_read):
	cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title, author, year, year_read))
	connection.commit()



print(search(title="A"))
