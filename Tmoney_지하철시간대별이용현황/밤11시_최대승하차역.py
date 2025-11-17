import csv
f = open('subwaytime.csv', encoding='utf-8')
data=csv.reader(f)
next(data)
next(data)

max = 0

max_station =''
t = int(input('몇시의 승차인원이 가장 많은 역이 궁금하세요?(24시간형식): '))

for row in data:
    row[4:] = map(int, row[4:])
    a = row[4+(t-4)*2] #입력받은 시각의 승차인원값 추출하기
    if a>max:          #모든 데이터 탐색
        max=a
        max_station = row[3]+'('+row[1]+')'

print(max_station,max)