import time
import crawling
import soccerdata

while 1:
	crawling.getNews()
	soccerdata.putData()
	time.sleep(300)
