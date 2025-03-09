#!/usr/bin/python3
"""
This module defines a SQLAlchemy ORM model for the 'states' table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class State(Base):
    """
    A class used to represent a State.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): The primary key of the state.
        name (str): The name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column("name", String(128))
