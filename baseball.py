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

  
a=[60100, 60181, 60264, 60304, 60336, 60343, 60404, 60456, 60496, 60523, 60558, 60636, 60648, 60658, 60667, 60724, 60865, 61102, 61194, 61208, 61323, 61353, 61363, 61366, 61463, 61554, 61643, 61666, 61700, 61742, 61743, 61893, 61895, 62007, 62016, 62147, 62164, 62265, 62332, 62349, 62404, 62409, 62415, 62558, 62655, 62864, 62893, 62907, 62929, 62931, 62934, 62947, 62966, 62967, 63077, 63088, 63248, 63440, 63448, 63512, 63559, 63593, 63634, 63636, 63698, 63700, 63704, 63913, 63935, 63959, 64001, 64004, 64006, 64007, 64012, 64013, 64017, 64022, 64041, 64085, 64086, 64117, 64153, 64158, 64166, 64300, 64346, 64440, 64499, 64504, 64560, 64602, 64610, 64646, 64657, 64699, 64706, 64717, 64804, 64906, 64914, 64944]
b=[65005, 65040, 65048, 65052, 65103, 65104, 65115, 65136, 65203, 65233, 65357, 65506, 65513, 65515, 65523, 65643, 65653, 65659, 65707, 65733, 65762, 65823]
c=[70224, 70410, 70553, 70646, 70756, 70839, 71118, 71184, 71207] 
d=[71255, 71347, 71432, 71504, 71552, 71562, 71565, 71610] 
e=[71752, 71815, 71835, 71837, 71842, 71848, 71857, 72133, 72214, 72261, 72303, 72324, 72443, 72447, 72456, 72523, 72546, 72551, 72559, 72749, 72860, 73113, 73136, 73153, 73209, 73211, 73213, 73306, 73339, 73342, 73543, 73602, 73606, 73703, 73750, 73824, 74103, 74148, 74158, 74163, 74167, 74206, 74215, 74223, 74339, 74358, 74465, 74540, 74605, 74729, 74745, 74756, 74823, 74846, 74857]

   
# 75000~79999
   
f = [75125]
g= [75151, 75334, 75441, 75620, 75808, 75847, 76100, 76119, 76158, 76232, 76249, 76267, 76290, 76313, 76322, 76368, 76404, 76435, 76509, 76536, 76720, 76746, 76753, 76757, 76802, 76812, 76822, 76849, 76854, 76869, 77104, 77147, 77243, 77248, 77318, 77454, 77462, 77463, 77532, 77564, 77609, 77623, 77648, 77669, 77848, 77854, 78122, 78168, 78217, 78224, 78242, 78248, 78288, 78352, 78366, 78454, 78467, 78517, 78536, 78548, 78629, 78666, 78753, 78760, 78765, 78813, 78823, 78850, 78892, 79109, 79113, 79130, 79192, 79198, 79215, 79231, 79234, 79240, 79290, 79300, 79356, 79365, 79402, 79453, 79456, 79530, 79705, 79760, 79869]
  
# 90000~99999'
  
h = [94629, 95158] 
i = [95436, 95657, 96307, 96610, 97109, 97202, 97336] 
j = [98144, 99222, 99507, 99563, 99606, 99737, 99810]

player=a+b+c+d+e+f+g+h+i+j
for k in player:
    player_all=basecraw("http://www.koreabaseball.com/Record/Player/HitterDetail/Total.aspx?playerId="+str(k))
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
        header=[]
        header.append("year")
        header.append("team")
        
        for i in range(len(head[0].select("a"))):
            header.append(head[0].select("a")[i].string)
        header.append("name")
        header.append("career")
        for i in range(len(header)):
            sheet1.write(row, i, header[i])
            
            if (i+1)%23 == 0:
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
                if (i+1)%21 == 1:
                	career = int(mid[0].select("td")[i].text)-int(mid[0].select("td")[0].text)
                	print career

                if (i+1)%21 == 0:
                    sheet1.write(row, 21, playername[0].text)
                    sheet1.write(row, 22, career)

                    row=row+1
                    col=0
                    career=0
                 
                   
             
            print playername[0].string, "ok"

 
book.save("player_vs.xls")
