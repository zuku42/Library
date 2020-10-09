import sqlite3

def connect(func):
	"""
	This is a decorator that connects to the library
	database, performs operations on the records of
	the database according to the instructions of the
	function it is decorating and closes the connection
	with the database.
	"""
	def wrapper_connect(*args, **kwargs):
		conn = sqlite3.connect("library_database.db")
		cur = conn.cursor()
		returned_value = func(cur, conn, *args, **kwargs)
		conn.close()
		return returned_value
	return wrapper_connect

@connect
def create_table(cursor, connection):
	"""
	Creates the table in the database if it does not
	already exist.
	"""
	cursor.execute("CREATE TABLE if not EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, year_read INTEGER)")
	connection.commit()

@connect
def view(cursor, connection):
	"""Returns all records of the database"""
	cursor.execute("SELECT * FROM books")
	rows = cursor.fetchall()
	return rows

@connect
def search(cursor, connection, title="", author="", year="", year_read=""):
	"""
	Returns all records of the database that meet 
	the search criteria.
	"""
	cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR year_read=?",(title, author, year, year_read))
	rows = cursor.fetchall()
	return rows

@connect
def insert(cursor, connection, title, author, year, year_read):
	"""
	Inserts new record into the database
	"""
	cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title, author, year, year_read))
	connection.commit()

@connect
def update(cursor, connection, id, title, author, year, year_read):
	"""
	Updates one of the records of the database based
	on its id
	"""
	cursor.execute("UPDATE books SET title=?, author=?, year=?, year_read=? WHERE id=?",(title, author, year, year_read, id))
	connection.commit()

@connect
def delete(cursor, connection, id):
	"""
	Deletes one of the records of the database based
	on its id
	"""
	cursor.execute("DELETE FROM books WHERE id=?",(id,))
	connection.commit()

@connect
def clear(cursor, connection):
	"""
	Clears the database
	"""
	cursor.execute("DELETE FROM books")
	connection.commit()

