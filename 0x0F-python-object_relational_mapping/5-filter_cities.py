#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def fetch_states(username, password, database, state_name):
    """
    Lists all states from the specified database that match the given state_name.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cur = db.cursor()

    # Execute SQL query with state_name as a parameter
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (state_name,))

    # Fetch all rows and print the results
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    # Close the cursor and disconnect from the server
    cur.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        fetch_states(username, password, database, state_name)
    else:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))

