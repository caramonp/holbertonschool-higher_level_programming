#!/usr/bin/python3
"""[script that lists all cities from the database hbtn_0e_4_usa]
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

    # execute SQL only recive %s
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")

    # Fetch a single row using fetchone() method
    for state in cursor.fetchall():
        print(state)

    # disconnect from server
    cursor.close()
    db.close()
