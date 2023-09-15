#!/usr/bin/python3

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbName = sys.argv[3]

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=username,
    passwd=password,
    db=dbName
)
cur = db.cursor()
cur.execute('SELECT * FROM states ORDER BY states.id')

states = cur.fetchall()
for state in states:
    print(state)

cur.close()
db.close()
