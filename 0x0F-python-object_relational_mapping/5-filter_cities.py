#!/usr/bin/python3
"""[a script that takes in the name of a state as an argument
|||||and lists all cities]
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
    cursor.execute("SELECT cities.name FROM cities\
                    JOIN states ON state_id=states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (argv[4],))

    # Fetch a single row using fetchone() method
    cities_in_state = cursor.fetchall()
    print(", ".join(row[0] for row in cities_in_state))

    # disconnect from server
    cursor.close()
    db.close()
