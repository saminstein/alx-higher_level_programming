from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()


users = session.query(User).all()

users.name = "Samuel Shielu"

session.commit()

print(users)