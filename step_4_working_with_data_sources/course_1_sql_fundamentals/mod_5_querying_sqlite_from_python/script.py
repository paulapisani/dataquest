import sqlite3

conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

query = 'SELECT Major, Major_category FROM recent_grads'
cursor.execute(query)
five_results = cursor.fetchmany(5)
