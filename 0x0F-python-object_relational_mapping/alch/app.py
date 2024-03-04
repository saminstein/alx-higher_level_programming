from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()


users = session.query(User).all()

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}")