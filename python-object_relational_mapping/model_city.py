#!/usr/bin/python3
"""
This module defines a SQLAlchemy ORM model for the 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    A class used to represent a City.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): The primary key of the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the state.
        state (relationship): The relationship to the State model.
    """
    __tablename__ = "cities"
    id = Column(
        "id", Integer, primary_key=True, nullable=False, autoincrement=True
        )
    name = Column("name", String(128), nullable=False)
    state_id = Column(
        "state_id", Integer, ForeignKey("states.id"), nullable=False
        )
    state = relationship("State", back_populates="cities")
