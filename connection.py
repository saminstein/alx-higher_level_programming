import MySQLdb

db=MySQLdb.connect (
        host="localhost",
        user="root",
        passwd="einstein2",
        database="saminstein"
        )

mycursor = db.cursor()

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
