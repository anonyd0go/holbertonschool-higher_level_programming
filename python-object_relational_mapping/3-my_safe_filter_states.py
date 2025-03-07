#!/usr/bin/python3
"""
Script that displays all values in the states table where name exactly matches the argument.
Safe from SQL injection and case-sensitive.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states \
        WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
