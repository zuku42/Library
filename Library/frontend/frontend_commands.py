import sys
sys.path.insert(0, '../backend')
import backend_methods as lb
from tkinter import *
def get_selected_row(event):
	global selected_id
	try:
		index=list1.curselection()[0]
		selected_id=list1.get(index)[0]
		e1.delete(0,END)
		e1.insert(END,list1.get(index)[1])
		e3.delete(0,END)
		e3.insert(END,list1.get(index)[2])
		e2.delete(0,END)
		e2.insert(END,list1.get(index)[3])
		e4.delete(0,END)
		e4.insert(END,list1.get(index)[4])
	except IndexError:
		pass

def view_command(self):
	db_conn = lb.DatabaseConnection("library_backend")
	db_conn.insert("Olga","Bie",2007,2020)
	self.list1.delete(0,END)
	for row in db_conn.view():
		self.list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	for row in lb.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
		list1.insert(END,row)

def insert_command():
	lb.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	list1.insert(END,lb.view()[-1])

def delete_command():
	list1.delete(0,END)
	lb.delete(selected_id)
	for row in lb.view():
		list1.insert(END,row)

def update_command():
	list1.delete(0,END)
	lb.update(selected_id,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	for row in lb.view():
		list1.insert(END,row)

def clear_command():
	list1.delete(0,END)