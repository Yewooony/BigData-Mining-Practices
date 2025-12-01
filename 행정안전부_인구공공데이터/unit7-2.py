### 교수님 코드 

import csv
import math

f = open('age2.csv','r', encoding='utf-8')
data = csv.reader(f)
next(data)

result_m = []
result_f = []
result_sum = []

name = input('궁금한 동네(시단위)를 입력해주세요 : ')
size = []

flag = 0
for row in data :
    if (name in row[2]) : 
        #print('flag :', flag)
        if (flag == 0) :
            for i in row[8:119] : 
                result_m.append(int(i))
            for i in row[119:] : 
                result_f.append(int(i))
            flag = flag + 1    
        else :
            for i in range (111) :
                result_m[i] = result_m[i] + int(row[i+8])
                result_f[i] = result_f[i] + int(row[i+119])
            flag = flag + 1    

for i in range (111) :  
    size.append(math.sqrt(result_m[i] + result_f[i]))
            
import matplotlib.pyplot as plt
plt.style.use('ggplot')            
plt.rc('font', family = 'Malgun Gothic')
#plt.figure(figsize = (5,1), dpi=300)
plt.title(name +' 지역의 성별 인구 그래프')
plt.scatter(result_m, result_f, s=size, c = range(111), alpha = 0.5, cmap = 'jet')
plt.colorbar()
plt.plot(range(max(result_m)), range(max(result_m)), 'g')
plt.xlabel('남성인구수')
plt.ylabel('여성인구수')
plt.show()