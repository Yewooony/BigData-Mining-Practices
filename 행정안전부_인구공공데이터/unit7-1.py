import csv
f = open('age_20250930.csv')
data = csv.reader(f)
next(data)
result_m = []
result_f = []
result_sum = []
name1 = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
name2 = input('앗!!! 동일한 지역명이 여러개 있을 수 있으니, 광역단위(도, 시) 이름도 입력해주세요 :')

for row in data :
    #if (name1 in row[4]) : 
    if (name1 in row[4]) and (name2 in row[2]) : 
        for i in row[8:119] : 
            result_m.append(int(i))
        for i in row[119:] : 
            result_f.append(int(i))
#result_sum = result_m + result_f #리스트의 단순 연결
result_sum = [m + f for m, f in zip(result_m, result_f)]

import matplotlib.pyplot as plt
plt.style.use('ggplot')            
plt.rc('font', family = 'Malgun Gothic')
#plt.title(name1 +' 지역의 인구구조')
plt.title(name2 +' '+name1 +' 지역의 인구구조')
#plt.plot(result_m, label='연령별 남자 인구수')
#plt.plot(result_f, label='연령별 여자 인구수')
plt.plot(result_sum, color='blue', label='연령별 남여 인구수')
#plt.legend()
plt.bar(range(111), result_sum)
plt.show()
    
    
