#!/usr/bin/python3

"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    base_url = "mysql+mysqldb://{}:{}@localhost/{}"
    eng = create_engine(
        base_url.format(username, password, dbName),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=eng)
    session = Session()
    states = session.query(State).order_by(State.id)

    stateFound = False
    for state in states:
        if state.name == stateName:
            stateFound = True
            print(f"{state.id}")
            break
    if stateFound is False:
        print("Not found")
