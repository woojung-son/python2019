# python2019

# 본인의 과제명 작성

전기컴퓨터공학부 | 201724493 | 손우정



## 프로젝트 개요
교통사고는 예부터 한국인 사고원인의 높은 순위에 자리잡으며 우리들을 괴롭혀 왔습니다. 이는 시민들의 안전의식 미비와 더불어 사고정보의 부족에서 기인한다고 볼 수 있습니다. 수만건의 교통사고 중 사망사고를 중점으로 사고 원인과 발생위치, 사건 경위를 분석하여 제공할 수 있는 프로그램은 인명피해를 줄임과 동시에, 시민들의 삶의 질 향상에 도움을 줄 것으로 기대해 봅니다.


## 화면 구성
![Alt text](C:\Users\CSE_USER\Downloads\맵축소.png)
![Alt text1](C:\Users\CSE_USER\Downloads\시간대별사고횟수.png)
![Alt text2](C:\Users\CSE_USER\Downloads\요일별사고횟수.png)
![Alt text3](C:\Users\CSE_USER\Downloads\확대.png)


## 사용한 공공데이터 
[데이터보기](https://www.data.go.kr/dataset/15003493/fileData.do)

## 소스
* [링크로 소스 내용 보기](https://github.com/cybermin/python2019/blob/master/tes.py) 

* 요일별사고횟수
~~~python
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
~~~

* 시간별사고횟수
~~~python
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
~~~

* 사고장소표시
~~~python
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

    map_location.save('D:\map.html')dnlz
~~~
