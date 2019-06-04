#-*- coding: cp949 -*-
#-*- coding: utf-8 -*-

import math
import pandas as pd
import folium
import datetime
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

df = pd.read_csv('2019.csv', encoding='CP949')

#print(df['발생년월일시'])

#df1 = df.loc[df.발생년월일시 < 2017010200, ['발생년월일시']] #이걸 이용해서 input으로 수를 받아 그래프 그리기 사용가능
#3plt.plot()

#print(df.발생년월일시.str[:4])

#-----------------------------
#input을 통해 월별, 일별, 주간별, 시간별 이런식으로 그래프를 그리기
#처음에 switch-case문으로 '월별'vs'일별'그래프를 선택하게 한다
#두번째로 월(1~12)를 입력받고, 일(월~일)을 입력받는다

#월별 만들어보기(1월달을 기준으로)
#df['D'] = df[str(df.발생년월일시)]
#print(df['D'])




#for i in range(len(df_time)) :
#    df_time.columns.values[i] = df_time.columns.values[i] % 100

#df_datelist = df.loc[(round(df.발생년월일시/ 10000) <= 2017010000 + i*100 + 24),
#              (round(df.발생년월일시/ 10000) >= 2017010000 + i*100), ['발생분']]
#print(numAcc)
#print(timeAcc)

#print(df_num_time)
#numacc = []
#for i in range(1,32) :
#    numacc.append(df.loc[(df.발생년월일시 <= 2017010000 + i*100 + 24), ['발생분']])
#print(numacc)

#df_numacc =
#plt.plot(range[1:32], 'bo-')
#df_temp = df
#df_temp["발생년월일시"] = df_temp["발생년월일시"] / 10000
#print(df_temp)
print(1)
#print(df_datelist)

def getDayName(a, b) :
    dayString = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return dayString[datetime.date(2017, a, b).weekday()]

def generateWeeklyGraph(x) :
    x = round(x/100)

    week = {'Sun':0, 'Mon':-1, 'Tue':-2, 'Wed':-3, 'Thu':-4, 'Fri':-5, 'Sat':-6}
    weekKor = ['일', '월', '화', '수', '목', '금', '토']
    numAcc = []
    sumAcc = []
    offset = week[getDayName(round((x%10000)/100), round(x%100))]
    for i in range(offset, offset+7) :
        #numAcc.append(list(df.loc[round(df.발생년월일시/ 100) == x1+i, '발생분'].values))
        sumAcc.append(sum(list(df.loc[round(df.발생년월일시/ 100) == x+i, '발생분'].values)))

    plt.plot(weekKor, sumAcc, 'bo-')
    plt.xlabel('사고요일')
    plt.ylabel('사고횟수')
    plt.title('요일별 사고횟수')
    plt.show()

def generateDailyGraph(x) :
    x = round(x/100)
    numAcc = df.loc[round(df.발생년월일시/ 100) == x, '발생분'].values
    timeAcc = df.loc[round(df.발생년월일시/ 100) == x, '발생년월일시'].values
    hourAcc = [i%100 for i in timeAcc]


    plt.plot(hourAcc, numAcc, 'bo-')
    plt.xlabel('사고시간')
    plt.ylabel('사고횟수')
    plt.title('시간대별 사고횟수')
    plt.show()

def generateMap(x) :
    location = {}
    location_arr = []
    location_arr2 = []
    latitude = (df.loc[df.발생년월일시 == x]['위도']).values
    longitude = df.loc[df.발생년월일시 == x]['경도'].values
    for i in range(len(latitude)) :
        location[latitude[i]] = longitude[i]
    for i in range(len(latitude)) :
        temp = []
        temp.append(list(location.keys())[i])
        temp.append(list(location.values())[i])
        location_arr.append(temp)

    if(len(location_arr) == 0) :
        print('There is no accident at that time')

    return ;
    #print(location)
    #print(location_arr)

    map_location = folium.Map(location=[list(location.keys())[0],
                list(location.values())[0]], zoom_start=7)

    folium.CircleMarker(location=location_arr[0], radius=100,
                        color='#3186cc', fill_color='#3186cc').add_to(map_location)
    #print('len(location_arr) : ', len(location_arr))
    for i in range(len(location_arr)) :
        folium.Marker(location_arr[i]).add_to(map_location)

    map_location.save('D:\map.html')
    #print(latitude)
    #print(longitude)
    #print(list(location.keys())[0])
    #print(list(location.values())[0])


month = int(input('월을 입력하세요'))
date = int(input('날짜를 입력하세요'))
hour = int(input('시간을 입력하세요'))
time = 2017000000 + month*10000 + date*100 + hour
generateDailyGraph(time)
generateWeeklyGraph(time)
generateMap(time)

