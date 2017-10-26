from urllib.request import urlopen
import re
import json

# 네이버 스포츠 해외 축구 최신뉴스
url = 'http://sports.news.naver.com/wfootball/news/index.nhn'

# http 응답 객체 생성
# 웹 페이지 전체 소스 코드 가져오기
f = urlopen(url)
buf = f.read().decode('utf-8')
f.close()

# 원하는 데이터가 들어 있는 json 객체를 정규식을 이용해서 파싱! 
p = re.compile('(newsListModel)(.*)')
m = p.search(buf)
data = m.group(2)[2:]

# json 모듈이 이용하여 사전 객체로 변환하기
data2 = json.loads(data)
data3 = data2['list']

# link 만들기!
link_base = "http://sports.news.naver.com/wfootball/news/read.nhn?oid=%s&aid=%s"

# key 가 title, aid, oid 인 것의 value 값 파싱!
n = 1
for i in data3 :
	# 원하는 값인 oid 와 aid 를 따로 변수에 담는다.
	oid = i['oid']
	aid = i['aid']
	link = link_base % (oid, aid)
	print(('%d 번째 링크 : ' %n), link)

	for a,b in i.items():
		if a == 'title':
			print(('%d 번째 기사 : ' %n), b)
			n+=1
