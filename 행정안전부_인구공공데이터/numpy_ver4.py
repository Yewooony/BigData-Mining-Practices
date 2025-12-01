import numpy as np
import csv
f = open('age2.csv','r', encoding='utf-8')
data = csv.reader(f)
next(data)
data = list(data)

name = input('인구구조가 알고싶은 지역의 이름(읍면동 단위)을 입력해주세요: ')

# 초기화
mn = 1
result_name =''
result = 0
home = None
result = None

# 궁금한 지역의 인구구조
for row in data:
    if name in row[4]:
        # 인덱스 8부터 끝까지의 인구수를 전체 인구수로 나누어 정규화 (NumPy 활용)
        population = np.array(row[8:], dtype=int)
        total_pop = int(row[5])

        # 시행착오1
        home_code = row[0]

        # 남녀 인구수를 요소별로 합산 후 정규화
        home_m = population[:111] # 남자 인구 데이터: 인덱스 0 ~ 110
        home_f = population[111:] # 여자 인구 데이터: 인덱스 111 ~ 221
        home_raw_sum = home_m + home_f
        home_sum = home_raw_sum / total_pop

# 비슷한 지역의 인구구조
for row in data:

    # 시행착오1: 자기 자신 제외 (행정기관코드 비교)
    if row[0] != home_code:

        # 다른 지역 (away)의 인구구조를 정규화
        population = np.array(row[8:], dtype=int)
        away_total_pop = int(row[5])

        # 남녀 분리 및 합산 후 정규화
        away_m = population[:111]
        away_f = population[111:]
        away_raw_sum = away_m + away_f
        away_sum = away_raw_sum / away_total_pop

        # 제곱 오차 합계 계산 (NumPy의 벡터화 연산)
        s = np.sum((home_sum - away_sum)**2)

        # 최소값 비교 및 업데이트
        if s < mn and name not in row[0]:
            mn = s
            result_name = row[2]+' '+row[3]+' '+row[4]+'('+row[0]+')'
            result_sum = away_sum # 합산된 데이터 저장

#궁금한 지역의 인구구조와 가장 비슷한 인구구조를 시각화한다
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name+' 지역과 가장 비슷한 인구구조를 가진 지역')

#plt.plot(home, label=name, color='blue')
#plt.plot(result, label=result_name, color='red', linestyle='--')

plt.plot(home_sum, label=name, color='blue')
plt.plot(result_sum, label=result_name, color='red', linestyle='--')

plt.legend()
plt.xlabel('연령대 (0세 ~ 110세 이상)')
plt.ylabel('인구 비율 (정규화 값)')
plt.show()
    