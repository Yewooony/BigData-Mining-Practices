import csv
f = open('subwaytime.csv', encoding='utf-8')
data=csv.reader(f)
next(data)
next(data)

max = [0]*24
max_station = ['']*24

for row in data:
    row[4:]=map(int, row[4:])
    for j in range(24):
        a=row[j*2+4] #j와 인덱스 번호 사이의 관계식 사용
        if a >max[j]:
            max[j] = a
            max_station[j] = row[3] 

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.bar(range(24),max)
plt.xticks(range(24), max_station, rotation=90)
plt.show()


