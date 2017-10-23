from urllib.request import urlopen
import re

# 정규식으로 title 부분 따오기
p = re.compile('<title>(.*)</title>')
url = 'http://sports.news.naver.com/wfootball/news/index.nhn'
f = urlopen(url)
buf = f.read()
buf2 = str(buf)
m = p.search(buf2)
print(m.group(1))

