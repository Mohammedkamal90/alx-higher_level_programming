#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve City objects sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        state_name = session.query(State.name).filter_by(id=city.state_id).scalar()
        print('{}: ({}) {}'.format(state_name, city.id, city.name))

    # Close the session
    session.close()
