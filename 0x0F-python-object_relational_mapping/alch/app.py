from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
# mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>"

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Base = declarative_base()

class user(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)