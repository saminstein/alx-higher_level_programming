#!/usr/bin/python3

from sys import argv
import MySQLdb


if __name__ == '__main__':
    '''
    Access the databass and lists all cities
    from the database
    '''

    db = MySQLdb.connect(
      host='localhost',
      user=argv[1],
      port=3306,
      passwd=argv[2],
      db=argv[3])

    cursor = db.cursor()
    cursor.execute("""
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id
    """)
    
    cities = cursor.fetchall()

    for city in cities:
        print(city)