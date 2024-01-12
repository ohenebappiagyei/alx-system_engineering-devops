#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    """
    Lists all cities for the given state from the specified database, sorted by id.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    c = db.cursor()

    # Execute SQL query to retrieve cities with the specified state
    c.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities "
              "JOIN states ON cities.state_id = states.id "
              "WHERE states.name = %s", (state_name,))

    # Fetch the result and print it
    result = c.fetchone()
    if result[0]:
        print(result[0])

    # Close the cursor and disconnect from server
    c.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        filter_cities_by_state(username, password, database, state_name)
    else:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
