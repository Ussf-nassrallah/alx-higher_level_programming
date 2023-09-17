#!/usr/bin/python3

"""
script that changes the name of a State
  object from the database hbtn_0e_6_usa
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

    target = session.query(State).filter_by(id=2).first()
    target.name = "New Mexico"
    session.commit()
    session.close()
