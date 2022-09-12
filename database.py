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

create_db = open("./create.sql", "r")

if ("museu",) not in databases:
  for line in create_db:
    if line.strip() != "":
      mycursor.execute(line.strip())
  print("Database created!")
create_db.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="museu"
)

mycursor = mydb.cursor()