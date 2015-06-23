import urllib2
from bs4 import BeautifulSoup
import csv

url = "http://kbodata.news.naver.com/m_rank/rank_batter.asp"
f = urllib2.urlopen(url)
page = f.read().decode('cp949', 'ignore')
f.close()

soup = BeautifulSoup(page)
a = soup.select('.table_board2 > tbody > tr')
b=[]
# for i in range(49):
	# print a[i].text.encode("utf-8")

b=a[1].text.encode("utf-8")
c=b.replace(" ","")
print c
# for i in range(8):
#    img = a[i].text
#    print img.encode("utf-8")
d = open("output.txt", "w")

d.write(str(a[1].text.encode("utf-8")) + "\n")
d.close()
