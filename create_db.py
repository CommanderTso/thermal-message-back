import sqlite3

db_file = 'thermal_printer_db.sqlite'

conn = sqlite3.connect(db_file)
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS users ( \
	id INTEGER PRIMARY KEY NOT NULL, \
	email TEXT NOT NULL, \
	first_name TEXT NOT NULL, \
	password TEXT NOT NULL)')

conn.commit()
conn.close()