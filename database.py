import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

databases = []

for x in mycursor:
  databases.append(x)

if "museu" not in databases:
  mycursor.execute("CREATE DATABASE museu")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="museu"
)

mycursor = mydb.cursor()