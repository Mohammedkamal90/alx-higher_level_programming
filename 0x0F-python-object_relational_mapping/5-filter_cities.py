#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa (SQL injection free!)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve cities of the specified state
    query = """
        SELECT GROUP_CONCAT(name ORDER BY id ASC SEPARATOR ', ')
        FROM cities
        WHERE state_id = (SELECT id FROM states WHERE name = %s)
        ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Print the result
    if result:
        print(result)
    else:
        print("")

    # Close the cursor and database connection
    cursor.close()
    db.close()
