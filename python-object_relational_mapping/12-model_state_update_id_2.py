#!/usr/bin/python3
"""
Script that changes the name of a State object from the database
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

    update_state = session.query(State).filter_by(id=2).first()

    if update_state:
        update_state.name = "New Mexico"

        session.commit()
    else:
        print("State with id=2 not found")

    session.close()
