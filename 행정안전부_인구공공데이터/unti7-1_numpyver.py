import csv
import numpy as np
import matplotlib.pyplot as plt

# 1. 파일 열기 및 헤더 건너뛰기
# 인코딩은 utf-8로 시도하고 실패 시 cp949로 재시도합니다.
try:
    f = open('age2.csv', mode='r', encoding='utf-8')
    data = csv.reader(f)
    next(data)
except UnicodeDecodeError:
    f = open('age2.csv', mode='r', encoding='cp949')
    data = csv.reader(f)
    next(data)

# 2. 사용자 입력
name1 = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
name2 = input('앗!!! 동일한 지역명이 여러개 있을 수 있으니, 광역단위(도, 시) 이름도 입력해주세요 :')

# 3. 데이터 찾기 및 NumPy 배열 생성
result_m = None
result_f = None

for row in data:
    if (name1 in row[4]) and (name2 in row[2]):
        male_data_list = row[8:119]
        female_data_list = row[119:]
        
        # NumPy 배열로 변환
        result_m = np.array(male_data_list, dtype=int)
        result_f = np.array(female_data_list, dtype=int)
        
        break

f.close()

if result_m is None:
    print(f"오류: '{name2} {name1}' 지역의 데이터를 찾을 수 없습니다.")
else:
    # 4. NumPy 계산
    result_sum = result_m + result_f

    # 5. 시각화 (선 그래프)
    plt.style.use('ggplot')
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False 

    plt.figure(figsize=(10, 6))
    plt.title(f'{name2} {name1} 지역의 인구구조 (NumPy 선 그래프)')

    # X축 연령대 (0부터 110세 이상)
    age_range = np.arange(len(result_sum))

    # 선 그래프로 출력
    plt.plot(age_range, result_sum, color='blue', label='연령별 남여 인구수')

    plt.xlabel('연령 (0세 ~ 110세 이상)')
    plt.ylabel('인구 수')
    plt.xticks(np.arange(0, 111, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()