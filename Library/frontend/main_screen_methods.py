import tkinter as tk


def get_selected_row(self, event):
	try:
		index = self.list1.curselection()[0]
		self.selected_id = self.list1.get(index)[0]
		self.e1.delete(0, tk.END)
		self.e1.insert(tk.END, self.list1.get(index)[1])
		self.e2.delete(0, tk.END)
		self.e2.insert(tk.END, self.list1.get(index)[2])
		self.e3.delete(0, tk.END)
		self.e3.insert(tk.END, self.list1.get(index)[3])
		self.e4.delete(0, tk.END)
		self.e4.insert(tk.END, self.list1.get(index)[4])
	except IndexError:
		pass

def view_command(self):
	self.list1.delete(0, tk.END)
	for row in self.db_conn.view():
		self.list1.insert(tk.END, row)

def search_command(self):
	self.list1.delete(0, tk.END)
	for row in self.db_conn.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.year_read_text.get()):
		self.list1.insert(tk.END, row)

def insert_command(self):
	self.db_conn.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.year_read_text.get())
	self.list1.insert(tk.END, self.db_conn.view()[-1])

def delete_command(self):
	self.list1.delete(0, tk.END)
	self.db_conn.delete(self.selected_id)
	for row in self.db_conn.view():
		self.list1.insert(tk.END, row)

def update_command(self):
	self.list1.delete(0, tk.END)
	self.db_conn.update(self.selected_id, self.title_text.get(), self.author_text.get(), self.year_text.get(), self.year_read_text.get())
	for row in self.db_conn.view():
		self.list1.insert(tk.END, row)

def clear_command(self):
	self.list1.delete(0, tk.END)
	for entry in (self.e1, self.e2, self.e3, self.e4):
		entry.delete(0, tk.END)