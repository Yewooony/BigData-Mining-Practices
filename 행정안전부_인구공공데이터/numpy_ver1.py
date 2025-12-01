import numpy as np
import csv

f = open('age2.csv','r', encoding='utf-8')
data = csv.reader(f)
next(data)

result_m = []
result_f = []
result_sum = []

name=input('인구구조가 알고싶은 지역의 이름(읍면동 단위)을 입력해주세요: ')
size = []

flag = 0
for row in data:
    if name in row[4]:
        if (flag == 0) :
            for i in row[8:119] : 
                home =  np.array(row[8:108], dtype=int)
            for i in row[119:] : 
                home2 =  np.array(row[109:-1], dtype=int)
        else :
            for i in range (111) :
                result_m[i] = result_m[i] + int(row[i+8])
                result_f[i] = result_f[i] + int(row[i+119])
            flag = flag + 1

for i in range (111) :  
    size.append(math.sqrt(result_m[i] + result_f[i]))
        

print(home)
print(home2)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title(name+' 지역의 인구구조')
plt.plot(home)
plt.plot(home2)
plt.show()