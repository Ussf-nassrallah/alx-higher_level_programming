#!/usr/bin/python3
"""
script that creates the State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    base_url = "mysql+mysqldb://{}:{}@localhost/{}"
    eng = create_engine(
        base_url.format(username, password, dbName),
        pool_pre_ping=True
    )

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()

    sess.add(City(name="San Francisco", state=State(name="California")))
    sess.commit()
    sess.close()
