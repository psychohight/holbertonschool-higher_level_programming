#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
