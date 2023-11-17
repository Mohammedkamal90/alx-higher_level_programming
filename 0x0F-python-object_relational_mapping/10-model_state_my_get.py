#!/usr/bin/python3
"""Script that prints the State object with the name passed as an argument
   from the database hbtn_0e_6_usa (SQL injection free)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve the State object with the specified name
    result = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()
