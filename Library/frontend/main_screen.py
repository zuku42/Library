import tkinter as tk


class MainScreen:
	from frontend_commands import view_command

	def __init__(self, master):
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
		title_text = tk.StringVar()
		author_text = tk.StringVar()
		year_text = tk.StringVar()
		year_read_text = tk.StringVar()

		#add entry boxes
		e1 = tk.Entry(self.master, textvariable=title_text)
		e2 = tk.Entry(self.master, textvariable=author_text)
		e3 = tk.Entry(self.master, textvariable=year_text)
		e4 = tk.Entry(self.master, textvariable=year_read_text)

		#position the entry boxes
		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)
		e3.grid(row=0, column=3)
		e4.grid(row=1, column=3)

		#add and position the listbox
		self.list1 = tk.Listbox(self.master, height=6, width=35)
		self.list1.place(x=20, y=60, width=220, height=120)

		#add buttons
		b1 = tk.Button(self.master, text="View all", width=10, command=self.view_command)
		b2 = tk.Button(self.master, text="Search entry", width=10)
		b3 = tk.Button(self.master, text="Add entry", width=10)
		b4 = tk.Button(self.master, text="Update", width=10)
		b5 = tk.Button(self.master, text="Delete", width=10)
		b6 = tk.Button(self.master, text="Clear list", width=10)

		#position the buttons
		b1.grid(row=2, column=3)
		b2.grid(row=3, column=3)
		b3.grid(row=4, column=3)
		b4.grid(row=5, column=3)
		b5.grid(row=6, column=3)
		b6.grid(row=7, column=3)

root = tk.Tk()
app = MainScreen(root)
root.mainloop()