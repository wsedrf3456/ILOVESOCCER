from urllib.request import urlopen

url = 'http://sports.news.naver.com/wfootball/news/index.nhn'
f = urlopen(url)
b = f.read()
print(b)
