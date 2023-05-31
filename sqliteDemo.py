import sqlite3

def list():
    connection = sqlite3.connect("chinook/chinook.db")
    cursor = connection.execute("select CustomerId,FirstName,LastName from customers")

    for line in cursor:
        print(line[2])

    connection.close()

list()