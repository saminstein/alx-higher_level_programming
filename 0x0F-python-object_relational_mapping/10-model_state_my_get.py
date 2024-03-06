#!/usr/bin/python3

"""
Write a script that prints the State object 
with the name passed as argument from the 
database hbtn_0e_6_usa
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

    states = session.query(State).format(State.name == argv[4])
    
    for state in states:
        print('{0}: {1}'.format(state.id, state.name))