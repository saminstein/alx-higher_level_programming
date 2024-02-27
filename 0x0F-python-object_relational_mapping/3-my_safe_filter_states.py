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
                    '%s' ORDER BY states.id ASC".format(argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)
        
    cursor.close()
    db.close()
