

##Connecting to what we learned in the backend tutorial to python
import sqlite3

#Y'all can insert file path to your database in place of '/Applications/localPlex.db'
conn = sqlite3.connect('/Applications/localPlex.db')
cursor = conn.cursor()

#Printing all the data in all the rows--replace users with the name of the table in your database.
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("")
print("")

#printing a specific data point of each row, say everyone's name. My users table is the one from the workshop, which has name age height weight etc
cursor.execute("SELECT name FROM users")
#fetchall returns a tuple
names = cursor.fetchall()
for name in names:
    #the reason I print name[0] instead of just name is that name is a tuple, and we really only want the first string
    print(name[0])




