#!/usr/bin/python3

'''
script that takes in an argument and displays
all values in the states table of
hbtn_0e_0_usa
where name matches the argument.
'''

from sys import argv
import MySQLdb


if __name__ == '__main__':
    '''
    Access the databass and gets the value
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
                    '{}' ORDER BY states.id ASC".format(argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)
