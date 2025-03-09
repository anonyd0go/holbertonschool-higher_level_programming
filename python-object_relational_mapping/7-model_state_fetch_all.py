#!/usr/bin/python3
"""
This script lists all State objects from the database 'hbtn_0e_6_usa'.
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

    connct = f'mysql+pymysql://{username}:{password}@localhost:3306/{database}'

    engine = create_engine(connct)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
