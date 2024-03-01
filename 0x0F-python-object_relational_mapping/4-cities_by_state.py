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
    cursor.execute("SELECT cities, states.id FROM cities ORDER BY cities.id ASC")
    
    states = cursor.fetchall()

    for cities in states:
        print(cities)