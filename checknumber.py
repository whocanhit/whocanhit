# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

  
def basecraw(url):
	f = urllib2.urlopen(url)
 	page = f.read()
 	f.close()
	soup = BeautifulSoup(page)
	return soup
player=[]
row=0
for k in range(69889,80000):
    player_all=basecraw("http://www.koreabaseball.com/Record/Player/HitterDetail/Game.aspx?playerId="+str(k))
    # print nckjh_all
    player_select = player_all.select(".player_records > table")
    #not ready table
    mid=player_select[0].select("tbody")
    #bring player name
#     playername = player_all.select("#cphContainer_cphContents_playerProfile_lblName")
#     beforeteam = player_all.select("#cphContainer_cphContents_playerProfile_lblCareer")
#     nowteam = player_all.select(".player_info > .team")
    #make content
#     y="LG".decode('utf-8')
    x = "데이터가 존재하지 않습니다.".decode('utf-8')
    #categolize team
    if x not in mid[0].select("td")[0].string:
        
#         if y in beforeteam[0].string:
#             if y not in nowteam[0].string:
                # exist player
#                 if playername[0].string:
                    #make content
        player.append(k)
        print "ok"
    print player,k
#stop at 68850
#[65005, 65040, 65048, 65052, 65103, 65104, 65115, 65136, 65203, 65233, 65357, 65506, 65513, 65515, 65523, 65643, 65653, 65659, 65707, 65733, 65762, 65823]
#upside thing is 65000~69889

#upside thing is 70000~73339