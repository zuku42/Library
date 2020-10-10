import tkinter as tk

from frontend.main_screen import MainScreen

if __name__ == "__main__":
	root = tk.Tk()
	app = MainScreen(root)
	root.mainloop()