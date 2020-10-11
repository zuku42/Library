"""
A DatabaseConnection class responsible for communication
with a SQLite database. Uses SQL commands imported from
the sql_commands.py module.
"""
import sqlite3

from backend.sql_commands import *


class DatabaseConnection:
	def __init__(self, db_name):
		"""Establish connection with the database"""
		self.conn = sqlite3.connect(db_name)
		self.cur = self.conn.cursor()
		self.create_table()
	
	def create_table(self):
		"""Create a table in the database"""
		self.cur.execute(CREATE_TEXT)
		self.conn.commit()

	def view(self):
		"""Return all records of the database"""
		self.cur.execute(VIEW_TEXT)
		rows = self.cur.fetchall()
		return rows

	def search(self, title="", author="", year="", year_read=""):
		"""Return records of the database that meet the search criteria"""
		self.cur.execute(SEARCH_TEXT, (title, author, year, year_read))
		rows = self.cur.fetchall()
		return rows

	def insert(self, title, author, year, year_read):
		"""Insert a new record into the database"""
		self.cur.execute(INSERT_TEXT, (title, author, year, year_read))
		self.conn.commit()

	def update(self, id, title, author, year, year_read):
		"""Update one of the records of the database based on its id"""
		self.cur.execute(UPDATE_TEXT,(title, author, year, year_read, id))
		self.conn.commit()

	def delete(self, id):
		"""Delete one of the records of the database based on its id"""
		self.cur.execute(DELETE_TEXT,(id,))
		self.conn.commit()

	def clear(self):
		"""Delete all records from the database"""
		self.cur.execute(CLEAR_TEXT)
		self.conn.commit()

	def close(self):
		"""Close connection with the database"""
		self.conn.close()
