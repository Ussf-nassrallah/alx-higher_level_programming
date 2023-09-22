#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

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
    sess = Session()

    states = sess.query(State).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
