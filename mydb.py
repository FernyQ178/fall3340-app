import mysql.connector

#Create data base connection with Django
database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'FQJr178801!',
	)

#middleware
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE 3340database")
print("Hello data base 3340data")