import sqlite3
# Import the sqlite3 Library
#  As a convention, we will show the SQL keywords in uppercase and the parts of the command that we are adding (such as the table and column names) will be shown in lowercase.

conn = sqlite3.connect('names.sqlite') # Connect to the file names.sqlite - If one doesn't exist, create one
cur = conn.cursor() # Create the cursor that allows us to do things in the db
cur.execute('DROP TABLE Names') # Delete the table to make a new one - Comment to disable this reset function
cur.execute('CREATE TABLE Names(name TEXT)')
cur.execute('INSERT INTO Names (name) VALUES (?)', ('None',)) # Create the default value. #
cur.execute('INSERT INTO Names (name) VALUES (?)', ('Yifan',))
cur.execute('INSERT INTO Names (name) VALUES (?)', ('Kelly',))
cur.execute('INSERT INTO Names (name) VALUES (?)', ('Brian',))
cur.execute('INSERT INTO Names (name) VALUES (?)', ('Devin',))
cur.execute('INSERT INTO Names (name) VALUES (?)', ('Tony',))
cur.execute('INSERT INTO Names (name) VALUES (?)', ('Regan',))

conn.commit() # Commit the new table. 

cur.execute('SELECT name FROM Names') # This returns a list at column names
for row in cur:
    print(row[0]) # Print the first thing in the tuple in the each row
#conn.commit()
conn.close()