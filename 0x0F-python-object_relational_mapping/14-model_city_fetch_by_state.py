#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    
    cities = session.query(City, State).join(State).all()
    
    for city, state in cities:
        print('{0}: {1} {2}'.format(state.name, city.name, city.name, ))
