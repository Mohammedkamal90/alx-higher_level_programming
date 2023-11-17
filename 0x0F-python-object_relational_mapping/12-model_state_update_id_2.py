#!/usr/bin/python3
"""Script that changes the name of a State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Query to retrieve the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State to "New Mexico"
    state_to_update.name = "New Mexico"

    # Commit changes to the database
    session.commit()

    # Close the session
    session.close()
