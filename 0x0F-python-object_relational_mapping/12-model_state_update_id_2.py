_#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    
    state_to_update = session.query(State).filter_by(id=2).first()
    
    if state_to_update:
        state_to_update.name = 'New Mexico'
        
        session.commit()
        print('{0}: {1}'.format(state_to_update.id, state_to_update.name)
        session.close()