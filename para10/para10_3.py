import sqlite3

connection = sqlite3.connect("para10_DB.sl3", 5)
cur = connection.cursor()

cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()
