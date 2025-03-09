#!/usr/bin/python3
"""
This script prints the first State object from the database 'hbtn_0e_6_usa'.
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: script.py <username> <password> <database>")
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    connct = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'

    engine = create_engine(connct)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
