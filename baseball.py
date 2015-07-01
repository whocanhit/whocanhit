# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import csv
  
def basecraw(url):
	f = urllib2.urlopen(url)
 	page = f.read()
 	f.close()
	soup = BeautifulSoup(page)
	return soup

for k in range(75124,75126):
    player_all=basecraw("http://www.koreabaseball.com/Record/Player/HitterDetail/Game.aspx?playerId="+str(k))
    # print nckjh_all
    player_select = player_all.select(".player_records > table")
    head = player_select[0].select("thead")
    #not ready table
    mid=player_select[0].select("tbody")
    #bring player name
    playername = player_all.select("#cphContainer_cphContents_playerProfile_lblName")
    beforeteam = player_all.select("#cphContainer_cphContents_playerProfile_lblCareer")
    nowteam = player_all.select(".player_info > .team")
    
    
    #bring header
    
    head = player_select[0].select("thead")
    #make header
    header=["구분"]
    for i in range(len(head[0].select("a"))):
            header.append(head[0].select("a")[i]['title'])
    import xlwt
    book = xlwt.Workbook(encoding="utf-8")
     #make sheet
    sheet1 = book.add_sheet("Sheet 1")
    #make content
    row=0
    sheet1.write(row, 16, "선수명") 
    for i in range(len(header)):
          
        sheet1.write(row, i, header[i])
        
        
    if (i+1)%16 == 0:
        row=row+1
     
    y="LG".decode('utf-8')
    x = "데이터가 존재하지 않습니다.".decode('utf-8')
    if x not in mid[0].select("td")[0].string:
        if y in beforeteam[0].string:
            if y not in nowteam[0].string:
                player_all=basecraw("http://www.koreabaseball.com/Record/Player/HitterDetail/Game.aspx?playerId="+str(k))
                # print player_all
                player_select = player_all.select(".player_records > table")
                head = player_select[0].select("thead")
                #not ready table
                mid=player_select[0].select("tbody")
                #bring player name
                playername = player_all.select("#cphContainer_cphContents_playerProfile_lblName")
                  
                if playername[0].string:
                    #make content
                    col=0
                    for i in range(len(mid[0].select("td"))):
                        sheet1.write(row, col, mid[0].select("td")[i].string)
                        col=col+1
                        
                        if (i+1)%16 == 0:
                            sheet1.write(row, 16, playername[0].string)
                            row=row+1
                            col=0
                        
                          
                    book.save("player_vs_75000_79999.xls")
                    print "ok"
    print k
