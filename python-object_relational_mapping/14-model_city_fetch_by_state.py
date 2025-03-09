#!/usr/bin/python3
"""
Script that prints all City objects from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <username> <password> <database>")
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    connct = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    engine = create_engine(connct, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}), {city.name}")

    session.close()
