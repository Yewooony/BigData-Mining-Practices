import csv
f = open('subwayfee.csv', encoding='utf-8')
data=csv.reader(f)
next(data)

label=['유임승차','유임하차','무임승차','무임하차']
c = ['#14CCC0','#389993','#FF1C6A','#CC14AF']

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    plt.figure(dpi=100)
    plt.title(row[3]+' '+row[1])
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3]+' '+'.png')
    plt.show()