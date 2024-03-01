#!/usr/bin/python3

'''
takes in the name of a state as an argument
and lists all cities of that state, using the 
database hbtn_0e_4_usa
'''

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
          SELECT 
              cities
          FROM
              states
          WHERE
              name LIKE %(state_name)s
          ORDER BY
              cities.id ASC
    """, {'state_name': argv[4]})
    
    cities = cursor.fetchall()

    for city in cities:
        print(cities)
