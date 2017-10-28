import sqlite3
import crawling

con = sqlite3.connect('soccer.db')
cur = con.cursor()

sql = 'insert into soccer values (?,?);'

records = crawling.getNews()
for record in records :
	cur.execute(sql,record)
con.commit()
con.close()
