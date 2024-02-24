import mysql.connector

mydb=mysql.connector.connect (
        host="localhost",
        user="root",
        password="einstein2",
        database="saminstein"
        )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
