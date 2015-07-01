# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import xlwt
book = xlwt.Workbook(encoding="utf-8")
 #make sheet
sheet1 = book.add_sheet("Sheet 1")


def basecraw(url):
	f = urllib2.urlopen(url)
 	page = f.read()
 	f.close()
	soup = BeautifulSoup(page)
	return soup
    
row=0


a = [75125]
b= [75151, 75334, 75441, 75620, 75808, 75847, 76100, 76119, 76158, 76232, 76249, 76267, 76290, 76313, 76322, 76368, 76404, 76435, 76509, 76536, 76720, 76746, 76753, 76757, 76802, 76812, 76822, 76849, 76854, 76869, 77104, 77147, 77243, 77248, 77318, 77454, 77462, 77463, 77532, 77564, 77609, 77623, 77648, 77669, 77848, 77854, 78122, 78168, 78217, 78224, 78242, 78248, 78288, 78352, 78366, 78454, 78467, 78517, 78536, 78548, 78629, 78666, 78753, 78760, 78765, 78813, 78823, 78850, 78892, 79109, 79113, 79130, 79192, 79198, 79215, 79231, 79234, 79240, 79290, 79300, 79356, 79365, 79402, 79453, 79456, 79530, 79705, 79760, 79869]
player_75000_79999 = a+b
for k in player_75000_79999:
    player_all=basecraw("http://www.koreabaseball.com/Record/Player/HitterDetail/Game.aspx?playerId="+str(k))
    # print nckjh_all
    player_select = player_all.select(".player_records > table")
    #bring header
    head = player_select[0].select("thead")
    #not ready table
    mid=player_select[0].select("tbody")
    #bring player name
    playername = player_all.select("#cphContainer_cphContents_playerProfile_lblName")
    beforeteam = player_all.select("#cphContainer_cphContents_playerProfile_lblCareer")
    nowteam = player_all.select(".player_info > .team")

    #make header only one time
    if row == 0:
        header=["구분"]
        for i in range(len(head[0].select("a"))):
                header.append(head[0].select("a")[i]['title'])
        sheet1.write(row, 16, "선수명") 
        for i in range(len(header)):
            sheet1.write(row, i, header[i])
            if (i+1)%16 == 0:
                row=row+1
     
#     y="LG".decode('utf-8')
    x = "데이터가 존재하지 않습니다.".decode('utf-8')
    #categolize team
    if x not in mid[0].select("td")[0].string:
#         if y in beforeteam[0].string:
#             if y not in nowteam[0].string:
                # exist player
        if playername[0].string:
            #make content
            col=0
            for i in range(len(mid[0].select("td"))):
                sheet1.write(row, col, mid[0].select("td")[i].text)
                col=col+1

                if (i+1)%16 == 0:
                    sheet1.write(row, 16, playername[0].text)
                    row=row+1
                    col=0
                
                  
            
            print playername[0].string, "ok"
        
    print k
book.save("player_vs_75000_79999.xls")