#!/usr/bin/python3

from sys import argv
from model_state import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    
    cities = session.query(City).order_by(cities.id).All()
    
    for city in cities:
        print('{0}: {1} {2}'.format(state.name, city.name, city.name, ))