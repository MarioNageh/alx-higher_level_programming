#!/usr/bin/python3
"""Task 0 Get all states from  states from the database alx"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """for make file not executable when imported"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_db_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=mysql_db_name)

    cur = db.cursor()
    cur.execute('''
        Select cities.id , cities.name , states.name from cities
        inner join states on cities.state_id = states.id
        order by cities.id asc
    ''')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
