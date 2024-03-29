#!/usr/bin/python3

"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    userInput = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=dbName
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

    cities = cur.fetchall()
    cities_arr = []
    for city in cities:
        if city[4] == userInput:
            cities_arr.append(city[2])

    print(", ".join(cities_arr))

    cur.close()
    db.close()
