import sqlite3

connection = sqlite3.connect("para10_DB.sl3", 5)
cur = connection.cursor()

cur.execute("UPDATE first_table SET name='Clif' WHERE rowid = 2;")
connection.commit()

connection.close()

