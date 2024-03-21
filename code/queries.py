import sqlite3

from vars import db_name



def query_cursor(cur, query):
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    print("")
    return None

def sql_queries():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    query = "SELECT * FROM Largest_banks"
    query2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
    query3 = "SELECT Name from Largest_banks LIMIT 5"

    query_cursor(cur, query)
    query_cursor(cur, query2)
    query_cursor(cur, query3)

    conn.close()
    return None