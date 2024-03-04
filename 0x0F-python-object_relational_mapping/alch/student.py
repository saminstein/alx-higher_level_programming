from sys import argv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

d_ul = "sqlite:///database.db"
engine = create_engine(d_ul)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))
    
Base.metadata.create_all(engine)
print(student)