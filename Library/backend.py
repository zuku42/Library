import sqlite3


class DatabaseConnection():

	def __init__(self, db_name):
		"""Establishes connection with the database"""
		self.conn = sqlite3.connect(db_name)
		self.cur = self.conn.cursor()
		self.create_table()
	
	def create_table(self):
		"""Creates a table in the database"""
		self.cur.execute("CREATE TABLE if not EXISTS books (id INTEGER PRIMARY KEY,\
						  title TEXT, author TEXT, year INTEGER, year_read INTEGER)")
		self.conn.commit()

	def view(self):
		"""Returns all records of the database"""
		self.cur.execute("SELECT * FROM books")
		rows = self.cur.fetchall()
		return rows

	def search(self, title="", author="", year="", year_read=""):
		 """Returns records of the database that 
		 	meet the search criteria"""
		self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=?\
						  OR year_read=?",(title, author, year, year_read))
		rows = self.cur.fetchall()
		return rows

	def insert(self, title, author, year, year_read):
		"""Inserts a new record into the database"""
		self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",\
					    (title, author, year, year_read))
		self.conn.commit()

	def update(self, id, title, author, year, year_read):
		"""Updates one of the records of the database 
			based on its id"""
		self.cur.execute("UPDATE books SET title=?, author=?, year=?, year_read=?\
						  WHERE id=?",(title, author, year, year_read, id))
		self.conn.commit()

	def delete(self, id):
		"""Deletes one of the records of the database
			based on its id"""
		self.cur.execute("DELETE FROM books WHERE id=?",(id,))
		self.conn.commit()

	def clear(self):
		"""Deletes all records from the database"""
		self.cur.execute("DELETE FROM books")
		self.conn.commit()

	def close(self):
		"""Closes connection with the database"""
		self.conn.close()