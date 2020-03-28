#https://medium.com/financeexplained/from-excel-to-databases-with-python-c6f70bdc509b
import sqlite3
import pandas as pd

dbname = 'FinanceExplainedDb'

conn = sqlite3.connect(dbname + '.sqlite')

df = pd.read_excel('wm.xls',sheet_name=None)

for table,df in df.items():
    df.to_sql(table,conn)
'''
df.to_sql(name='Table1',con=conn)

cur = conn.cursor()

cur.execute('SELECT * FROM Table1')

names = list(map(lambda x: x[0], cur.description))
print(names)

for row in cur:
    print(row)

cur.close()
'''
