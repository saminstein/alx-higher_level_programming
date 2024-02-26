import MySQLdb

db=MySQLdb.connect (
        host="localhost",
        user="root",
        passwd="einstein2",
        database="saminstein"
        )

print(db)
