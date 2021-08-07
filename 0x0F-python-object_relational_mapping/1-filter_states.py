#!/usr/bin/python3
"""[ lists all states with N from the database hbtn_0e_0_usa]
"""
import sys
import MySQLdb


if __name__ == "__main__":

    # Open DataBase
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a object with cursor method
    cursor = db.cursor()

    # execute SQL query using execute() method
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                    in ORDER BY id")

    # Fetch a single row using fetchone() method
    for row in cursor.fetchall():
        print(row)

    # disconnect from server
    cursor.close()
    db.close()
