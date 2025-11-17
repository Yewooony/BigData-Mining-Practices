import csv
import math
f = open('gender.csv', encoding='utf-8')
data = csv.reader(f)
next(data)

m=[]
fm=[]
sum = []
size=[]
name=input('궁금한 동네를 입력해주세요: ')

for row in data:
    if name in row[0]:
        for i in row[8:119]:
            m.append(int(i))
        for i in row[119:]:
            fm.append(int(i))

        for i in range(111):
            m[i] = m[i]+int(row[i+8])
            f[i] = f[i]+int(row[i+119])

for i in range (111):
    size.append(math.sqrt(m[i]+f[i]))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.figure(figsize=(10,5), dpi=100)
plt.title(name+' 지역의 성별 인구 그래프')
plt.scatter(m,fm,s=size,c=range(101),alpha=0.5,cmap='jet') 
plt.colorbar()
# 1:1 대각선 그리기 (X, Y축 길이 불일치 오류를 해결)
if m and fm:
    max_val = max(max(m), max(fm)) + 1 
    plt.plot(range(max_val), range(max_val), 'g')

plt.xlabel('남성인구수') 
plt.xlabel('여성인구수') 
plt.show()