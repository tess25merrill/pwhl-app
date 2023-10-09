#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(User).delete()
    session.commit()

    print("Seeding database...")

    users = [
        User(
            username=fake.word(),
            email=fake.email(),
        )
    for i in range(50)]

    session.add_all(users)
    session.commit()    
