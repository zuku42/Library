# Library - keep track of the books you have read

This is a desktop application that allows you to keep record of the books
you have read. It stores information about each of the books (including its
title, author, year of publication, and year you have read it) in a database
and enables you to communicate with it through a graphical user interface.
The functionality of the application allows you to display, add, update,
and delete particular records, as well as to search the database for books
matching particular criteria (e.g. all books I have read in 2018, or all
books written by Charles Bukowski in 1989).

# Installation

To run the application simply download the 'main.exe' file and place it in
a directory you find fitting. Upon the first start up, the database (named
"library_database.db") will be created in the same directory. It is not to
be deleted, as doing so will delete your data irreversibly.

Alternatively, it is also possible to run the application by downloading all
the code in the Library folder and, while keeping it in the same directory,
navigating to that directory from the command line and using a 'python' 
command to run the main.py file. For that to work, however, one needs to have
Python installed on their computers, along with the following libraries:
sqlite3, Tkinter. 

# Technology

This project was developed with Python 3.7. It was split into two packages:
backend and frontend.

The backend package contains two modules: backend_methods.py and
sql_commands.py. "backend_methods.py" contains a DatabaseConnection class 
responsible for the communication with the SQLite database, where the data
input by the users are stored. It uses sqlite3 library for that purpose.
The methods of the class use SQL commands (stored in the sql_commands.py
module for better readability of the code) to insert, delete, update or
fetch the records of a given database.

Similarly, the frontend package contains two modules: main_screen.py
and main_screen_methods.py. "main_screen.py" cotains a MainScreen class
developed with Tkinter that is responsible for the design of the main screen
of the application. Additional methods of the class, responsible for adding 
functionality to the interactive elements of the main screen using methods 
of the backend_methods.py module, can be found in the main_screen_methods.py.