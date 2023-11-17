#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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

    # Execute SQL query using format to create the query with user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
