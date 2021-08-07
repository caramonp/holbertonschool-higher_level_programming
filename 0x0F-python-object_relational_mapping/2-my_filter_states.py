#!/usr/bin/python3
"""[ lists all states with N from the database hbtn_0e_0_usa]
"""
import sys
from sys import argv
import MySQLdb


if __name__ == "__main__":

    # Open DataBase
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a object with cursor method
    cursor = db.cursor()

    # execute SQL query
    cursor.execute("SELECT * FROM states WHERE name = '{}'\
                    ORDER BY id ASC".format(argv[4]))

    # Fetch a single row using fetchone() method
    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)

    # disconnect from server
    cursor.close()
    db.close()
