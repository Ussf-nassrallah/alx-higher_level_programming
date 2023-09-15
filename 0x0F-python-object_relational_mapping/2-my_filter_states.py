#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    user_input = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=dbName
    )
    cur = db.cursor()

    q = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    cur.execute(q, (user_input,))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
