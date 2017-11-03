import sqlite3

def putData(records):
	# DB 연결, SQL 구문 호출 위해 객체 생성
	con = sqlite3.connect('soccer.db')
	cur = con.cursor()

	sql = 'insert into soccer values (?,?,?);'

	try :
		# 웹 페이지 data 들을 sql 형태에 맞게 넣기
		for record in records :
			cur.execute(sql,record)
	except :
		pass

	# 작업한 내용을 실제로 DB에 반영
	con.commit()

	# DB 연결 닫기
	con.close()
	return records
