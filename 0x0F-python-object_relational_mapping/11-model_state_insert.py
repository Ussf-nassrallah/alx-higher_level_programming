#!/usr/bin/python3

"""
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


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

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()

    print(newState.id)
    session.close()
