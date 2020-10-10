import tkinter as tk

from backend.backend_methods import DatabaseConnection
from frontend.main_screen import MainScreen


DATABASE_NAME = "library_database.db"

if __name__ == "__main__":
	database = DatabaseConnection(DATABASE_NAME)
	root = tk.Tk()
	app = MainScreen(root, database)
	root.mainloop()
	database.close()