import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

%matplotlib inline

conn = sqlite3.connect('factbook.db')
q = 'SELECT * FROM sqlite_master WHERE type = 'table''
pd.read_sql_query(q,conn)

query_1 = 'SELECT * FROM facts LIMIT 5'
pd.read_sql_query(query_1, conn)

query_2 = 'SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth) FROM facts'
pd.read_sql_query(query_2, conn)

query_3 = 'SELECT name FROM facts WHERE population = 0'
pd.read_sql_query(query_3, conn)

query_4 = 'SELECT population, population_growth, birth_rate, death_rate FROM facts'
data = pd.read_sql_query(query_4, conn)
data.hist()
