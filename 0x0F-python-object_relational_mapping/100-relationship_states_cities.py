#!/usr/bin/python3
"""Script that creates State “California” with City “San Francisco” from the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    new_state = State(name='California', cities=[City(name='San Francisco')])

    # Add the new State to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
