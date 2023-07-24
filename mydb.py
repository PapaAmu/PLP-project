import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword'
)

#this part is a cursor object
cursorObject = dataBase.cursor()




#Creating a database
cursorObject.execute("CREATE DATABASE siyamuza")
print("Database created successfully!")