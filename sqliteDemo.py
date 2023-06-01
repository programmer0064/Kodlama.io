import sqlite3

def list():
    connection = sqlite3.connect("chinook/chinook.db")
    cursor = connection.execute("select CustomerId,FirstName,LastName,Company,Address,City,State,Country,PostalCode,Phone,Fax,Email,SupportRepId from customers")

    for line in cursor:
        print(line[7])

    connection.close()

list()

"""First of all we imported the module for sqlite, which contains data packets like special functions etc. in order to interact with the sqlite database and execute different commands on that.
Then we defined a funtion which will list some sort of data from database. At first, we established a connection with sqlite chinook database in sqlite browser. Afterwards, with connection.execute
we tell the browser that he has to do something for us. With (select...) we tell him the range of data he has to permit access. With the for loop we will list every line in a certain column."""
#.cursor(): It's an object used to execute SQL statements and data set fetch operations.