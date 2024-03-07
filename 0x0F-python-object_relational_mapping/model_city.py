
#from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True);
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, FOREIGN KEY(state_id) REFERENCE state(id))