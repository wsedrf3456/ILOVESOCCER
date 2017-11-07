import time
import crawling
import soccerdata

while 1:
	records = crawling.getNews()
	soccerdata.putData(records)
	time.sleep(300)
