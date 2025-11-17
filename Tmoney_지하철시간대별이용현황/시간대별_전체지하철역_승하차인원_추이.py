import csv
f = open('subwaytime.csv', encoding='utf-8')
data=csv.reader(f)
next(data)
next(data)

s_in = [0]*24
s_out = [0]*24

for row in data:
    row[4:] = list(map(int, row[4:])) #데이터 접근을 위해 맵을 리스트화
    for i in range(24):
        s_in[i] += row[4 + i * 2]
        s_out[i] += row[5 + i *2]

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label = '승차')
plt.plot(s_out, label = '하차')
plt.legend()
# 0,1,2,3시로 하기 위한 라벨 추가
x_tick_labels = [(i + 4) % 24 for i in range(24)] 
plt.xticks(range(24), x_tick_labels)
plt.show()



