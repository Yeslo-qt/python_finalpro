import sqlite3

connection = sqlite3.connect("para10_DB.sl3", 5)
cur = connection.cursor()

cur.execute("INSERT INTO first_table (name) VALUES ('Lisa');")
cur.execute("INSERT INTO first_table (name) VALUES ('Dima');")
cur.execute("INSERT INTO first_table (name) VALUES ('Anna');")
connection.commit()

res = cur.fetchall()
print(res)

connection.close()
