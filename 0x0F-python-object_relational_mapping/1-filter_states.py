#!/usr/bin/python3
"""
Scripts that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""


import MySQLdb
from sys import argv


def filter_states(username, password, database):
    """
    Filter states and display results
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows and print them
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and disconnect from server
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    # Get MySQL username, password, and database name from command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Call the filter_states function
    filter_states(username, password, database)
