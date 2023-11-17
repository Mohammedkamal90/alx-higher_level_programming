#!/usr/bin/python3
"""Script that lists all City objects from database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

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

    # Query to retrieve all City objects
    query = session.query(City).order_by(City.id)

    # Loop through the results and print the information
    for city in query.all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
