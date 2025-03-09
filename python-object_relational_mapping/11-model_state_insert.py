#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()

    print(new_state.id)

    session.close()
