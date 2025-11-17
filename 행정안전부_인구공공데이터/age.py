import csv
f = open('age.csv','r', encoding='utf-8')
data = csv.reader(f)
next(data)

resultm = []
resultfm = []
name1 = input('인구 구조가 알고 싶은 지역의 이름(시도명 단위)을 입력해주세요: ')
name2 = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요: ')

for row in data: 
    if name1 in row[0] and name2 in row[2]: # 시도명이 있다면
        for i in row[6:117]: #남자 0~110세 구간
            resultm.append(int(i))
        for i in row[-111:]: #여자 0~110세 구간
            resultfm.append(int(i))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name2+' 지역의 인구 구조')
plt.plot(resultm, 'blue', label = 'Male')
plt.plot(resultfm, 'red', label = 'Female')
plt.legend()
plt.show()


