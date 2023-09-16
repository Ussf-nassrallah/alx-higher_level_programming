#!/usr/bin/python3

"""
python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This MySQL database state representation includes the following attributes:

    - __tablename__: The name of the MySQL table where state data is stored.
    - id: An integer field representing the unique identifier of the state.
    - name: A string field representing the name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
