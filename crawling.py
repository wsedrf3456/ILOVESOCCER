from urllib.request import urlopen
import re
import json

# 정규식으로 title 부분 따오기
p = re.compile('(newsListModel)(.*)')
url = 'http://sports.news.naver.com/wfootball/news/index.nhn'
f = urlopen(url)
buf = f.read().decode('utf-8')
m = p.search(buf)

# json 모듈이 이용하여 사전 객체로 변환하기
data = m.group(2)[2:]
data2 = json.loads(data)
data3 = data2['list']

# key 가 title 인 것의 value 값 따오기
n = 1
for i in data3 :
	for a,b in i.items():
		if a == 'title':
			print(('%d 번째 기사 : ' % n), b)
			n += 1
