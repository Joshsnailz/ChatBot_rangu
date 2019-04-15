import sqlite3

conn = sqlite3.connect("database.sqlite")
c = conn.cursor()

c.execute(""" SELECT * FROM May2015 WHERE id !='NULL' """)
print(c.fetchall())

conn.commit()
conn.close()
