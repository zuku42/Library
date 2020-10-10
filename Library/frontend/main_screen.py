"""
A MainScreen class responsible for the design
and the functionality of the app's main screen.
"""
import tkinter as tk


class MainScreen:
	#import other methods from main_screen_methods.py
	from frontend.main_screen_methods import (get_selected_row,
	view_command, search_command, insert_command, delete_command, 
	update_command, clear_command)

	def __init__(self, master, db_conn):
		"""
		An __init__ method responsible for outlining the
		elements of the main screen and assigning functionalities 
		of the other methods to particular interactive elements 
		of the main screen using the connection with the database
		passed as one of the arguments of the class.
		"""
		#database connection
		self.db_conn = db_conn

		#root of the app
		self.master = master
		self.master.wm_title("My library")
		
		#add labels
		l1 = tk.Label(self.master, text="Title")
		l2 = tk.Label(self.master, text="Author")
		l3 = tk.Label(self.master, text="Year published")
		l4 = tk.Label(self.master, text="Year read")

		#position the labels
		l1.grid(row=0, column=0)
		l2.grid(row=0, column=2)
		l3.grid(row=1, column=0)
		l4.grid(row=1, column=2)

		#placeholders for the user inputs
		self.title_text = tk.StringVar()
		self.author_text = tk.StringVar()
		self.year_text = tk.StringVar()
		self.year_read_text = tk.StringVar()

		#add entry boxes
		self.e1 = tk.Entry(self.master, textvariable=self.title_text)
		self.e2 = tk.Entry(self.master, textvariable=self.author_text)
		self.e3 = tk.Entry(self.master, textvariable=self.year_text)
		self.e4 = tk.Entry(self.master, textvariable=self.year_read_text)

		#position the entry boxes
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=0, column=3)
		self.e3.grid(row=1, column=1)
		self.e4.grid(row=1, column=3)

		#add, position and bind a method to the listbox
		self.list1 = tk.Listbox(self.master, height=6, width=35)
		self.list1.place(x=20, y=60, width=240, height=120)
		self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

		#add buttons and assign them methods
		b1 = tk.Button(self.master, text="View all", width=10, command=self.view_command)
		b2 = tk.Button(self.master, text="Search entry", width=10, command=self.search_command)
		b3 = tk.Button(self.master, text="Add entry", width=10, command=self.insert_command)
		b4 = tk.Button(self.master, text="Update", width=10, command=self.update_command)
		b5 = tk.Button(self.master, text="Delete", width=10, command=self.delete_command)
		b6 = tk.Button(self.master, text="Clear list", width=10, command=self.clear_command)

		#position the buttons
		b1.grid(row=2, column=3)
		b2.grid(row=3, column=3)
		b3.grid(row=4, column=3)
		b4.grid(row=5, column=3)
		b5.grid(row=6, column=3)
		b6.grid(row=7, column=3)