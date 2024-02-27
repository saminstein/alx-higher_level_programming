#!/usr/bin/python3

'''
script that lists all states with a name
starting with N (upper N) from the database
hbtn_0e_0_usa
'''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    '''
    Access the database and gets the state
    from the database
    '''

    db = MySQLdb.connect(
      host='localhost',
      user=argv[1],
      port=3306,
      passwd=argv[2],
      db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE states.name LIKE \
                    'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)
        
    cursor.close()
    db.close()
