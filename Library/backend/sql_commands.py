"""
SQL commands contained in this module are used
in the backend_commands.py module in the
DatabaseConnection class.
"""
CREATE_TEXT = "CREATE TABLE if not EXISTS books (id INTEGER PRIMARY KEY,\
				title TEXT, author TEXT, year INTEGER, year_read INTEGER)"
VIEW_TEXT = "SELECT * FROM books"
SEARCH_TEXT = "SELECT * FROM books WHERE title=? OR author=? OR year=? OR year_read=?"
INSERT_TEXT = "INSERT INTO books VALUES (NULL,?,?,?,?)"
UPDATE_TEXT = "UPDATE books SET title=?, author=?, year=?, year_read=? WHERE id=?"
DELETE_TEXT = "DELETE FROM books WHERE id=?"
CLEAR_TEXT = "DELETE FROM books"
