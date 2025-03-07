#!/usr/bin/python3
"""
Script that lists all states with names starting with 'N'
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
