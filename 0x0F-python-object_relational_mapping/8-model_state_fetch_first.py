#!/usr/bin/python3

"""
script that prints the first State object from 
the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    first_state = session.query(State).order_by(State_id).first()

    if first_state is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(states.id, states.name)