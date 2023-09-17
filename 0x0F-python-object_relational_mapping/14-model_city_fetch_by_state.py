#!/usr/bin/python3

"""
script that prints all City objects
  from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    base_url = "mysql+mysqldb://{}:{}@localhost/{}"
    eng = create_engine(
        base_url.format(username, password, dbName),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=eng)
    session = Session()
    data = session.query(City, State) \
        .filter(City.state_id == State.id) \
        .order_by(City.id)

    for city, state in data:
        print(f"{state.name}: ({city.id}) {city.name}")
