#!/usr/bin/python3
"""Task 0 Get all states from  states from the database alx"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """for make file not executable when imported"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_db_name = argv[3]
    name_to_search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=mysql_db_name)

    cur = db.cursor()
    cur.execute('''
    Select * from states where name = '{}' order by id asc
    '''.format(name_to_search))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
