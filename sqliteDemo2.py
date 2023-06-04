import sqlite3
import pandas as pd # pip install pandas   #module that provides functions to do data analysis

# Create a database
connection = sqlite3.connect('student.db')   #connects to database file and creates it automatically
# connection = sqlite3.connect(':memory:')   #connects and creates database temporarily that exists on ram

# Create a table - this what our table looks like
sql_create_table = """
CREATE TABLE students (
    student_id TEXT PRIMARY KEY,
    student_name TEXT NOT NULL,
    gender TEXT,
    major TEXT,
    year_enrolelr INTEGER,
    email TEXT UNIQUE
)   
"""

cursor = connection.cursor()   #object used to execute sql statements
try:
    cursor.execute(sql_create_table)   #to create a table we first need to commit the statement
    connection.commit()   #execute sql statement
except Exception as e:
    print(e)
    connection.rollback()  #if I run into any error, do not any operation


# Insert records
cursor = connection.cursor()  #execute another statement - we store the output in a seperate object to continue working with it
cursor.execute("INSERT INTO students VALUES ('A10031','student_name11','M','Computer Science',2022,'email1168468@gmail.com')")
cursor.execute("INSERT INTO students VALUES ('A10017','student_name77','M','Mathematics',2023,'email17@gmail.com')")
cursor.execute("INSERT INTO students VALUES ('A10052','student_name22','F','Biology',2021,'email13@gmail.com')")
cursor.execute("INSERT INTO students VALUES ('A10064','student_name44','M','Accounting',2018,'email14@gmail.com')")
cursor.execute("INSERT INTO students VALUES ('A10075','student_name55','F','Marketing',2019,'email15@gmail.com')")
cursor.execute("INSERT INTO students VALUES ('A10086','student_name66','F','Sociology',2022,'email16@gmail.com')")
connection.commit()             #we always need to commit sql statements

# Query records
sql_query = """
SELECT * FROM students LIMIT 5
"""
rows = cursor.execute(sql_query)
columns = [col[0] for col in rows.description]
records = rows.fetchall()
connection.close()
print(columns)
print(records)

df = pd.DataFrame(records, columns=columns)
print(df.to_csv('data.csv'))

"""
# Using WITH statement to auto close connections
from contextlib import closing
import sqlite3
import pandas as pd # pip install pandas

with closing(sqlite3.connect('demo.db')) as connection2:
    with closing(connection2.cursor()) as cursor2:
        cursor2.execute("INSERT INTO students VALUES ('A10001','student_name1','M','Computer Science',2022,'email1@gmail.com')")
        cursor2.execute("INSERT INTO students VALUES ('A10003','student_name3','M','English',2018,'email3@gmail.com')")
        cursor2.execute("INSERT INTO students VALUES ('A10002','student_name2','F','Biology',2021,'email2@gmail.com')")
        cursor2.execute("INSERT INTO students VALUES ('A10004','student_name4','M','Accounting',2018,'email4@gmail.com')")
        cursor2.execute("INSERT INTO students VALUES ('A10005','student_name5','F','Marketing',2019,'email5@gmail.com')")
        cursor2.execute("INSERT INTO students VALUES ('A10006','student_name6','F','Sociology',2022,'email6@gmail.com')")
        connection2.commit()

        sql_query2 = "SELECT * FROM students LIMIT 5"
        rows2 = cursor2.execute(sql_query)
        columns2 = [col[0] for col in rows2.description]
        records2 = rows2.fetchall()
        df = pd.DataFrame(records2, columns=columns2)
print(df)        
"""