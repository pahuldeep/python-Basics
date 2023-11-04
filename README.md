**README**

## Python Basics

This repository contains some basic Python code, including data algorithms, tkinter projects, and database management using MySQL.

### Data algorithms

* Trees
* Sorting
* Linked list

### tkinter projects

* Simple GUI applications with database connection and various functions

### MySQL database management

* Connecting to a MySQL database
* Creating and managing tables
* Inserting, updating, and deleting data
* Running queries

**Example usage:**

```python
# Import the necessary packages
import tkinter as tk
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(host='localhost', user='root', password='', database='my_database')

# Create a GUI window
root = tk.Tk()

# Create a label to display the database connection status
connection_status_label = tk.Label(root, text='Database connection status: {}'.format(db.is_connected()))

# Place the label on the window
connection_status_label.pack()

# Create a button to run a query on the database
query_button = tk.Button(root, text='Run query', command=lambda: run_query())

# Place the button on the window
query_button.pack()

# Start the mainloop
root.mainloop()

# Run a query on the database
def run_query():
    cursor = db.cursor()

    # Execute the query
    cursor.execute('SELECT * FROM users')

    # Get the results of the query
    results = cursor.fetchall()

    # Print the results to the console
    print(results)
```

**Contributing:**

If you have any suggestions or contributions, please feel free to create a pull request.
