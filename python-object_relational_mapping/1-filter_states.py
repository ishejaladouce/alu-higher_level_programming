#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database.
"""

import MySQLdb
import sys

def main():
    """Connects to the database and lists states starting with 'N'"""
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = db.cursor()

    # Execute SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
