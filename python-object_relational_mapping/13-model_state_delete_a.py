#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <username> <password> <database>")
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    connct = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    engine = create_engine(connct)

    Session = sessionmaker(bind=engine)
    session = Session()

    delete_states = session.query(State).filter(State.name.like('%a%')).all()

    for state in delete_states:
        session.delete(state)

    session.commit()
    session.close()
