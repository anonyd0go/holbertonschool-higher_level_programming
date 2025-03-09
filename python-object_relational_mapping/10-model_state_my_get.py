#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: script.py <username> <password> <database> <state>")
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    connct = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    engine = create_engine(connct)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
