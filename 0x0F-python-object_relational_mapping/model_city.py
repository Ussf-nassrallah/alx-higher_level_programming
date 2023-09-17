#!/usr/bin/python3

"""
Python file similar to model_state.py named model_city.py
  that contains the class definition of a City
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class:
      id: Int -> primary Key
      name: String
      state_id: Int -> foreign Key
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey("states_id"), nullable=True)
