import csv
f = open('subwaytime.csv', encoding='utf-8')
data=csv.reader(f)
next(data)
next(data) #중요

result=[]

for row in data:
    row[4:]=map(int,row[4:])
    result.append(sum(row[10:15:2])) #아침 7~9시

import matplotlib.pyplot as plt
result.sort() #오름차순 정렬
plt.figure(dpi=100)
plt.style.use('ggplot')
plt.bar(range(len(result)),result)
plt.show()

