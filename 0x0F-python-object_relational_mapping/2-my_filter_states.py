#!/usr/bin/python3
""" A script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY id".format(args[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
