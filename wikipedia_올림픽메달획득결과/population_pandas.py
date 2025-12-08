## 교수님 강의자료 참고하여 작성

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

df = pd.read_csv('age.csv', encoding='cp949', index_col=0)
df = df.div(df['총인구수'], axis=0)
del df['총인구수'], df['연령구간인구수'] # '총인구수'와 '연령구간인구수' 컬럼을 삭제

name = input('원하는 지역의 이름을 입력해주세요 : ')
a = df.index.str.contains(name) # 입력된 이름이 포함된 인덱스를 찾습니다.
df2 = df[a] # 해당 지역의 데이터만 필터링합니다.

# 입력된 지역(df2의 첫 번째 행)과의 연령별 인구 비율 차이의 제곱 합이 가장 작은
# 5개 지역을 찾아서(즉, 연령별 인구 구조가 가장 비슷한 5개 지역) 그래프로 시각화합니다.

x = df.sub(df2.iloc[0], axis=1)
y = np.power(x,2)
z = y.sum(axis = 1)

i = z.sort_values().index[:5]
df.loc[i].T.plot()

plt.show()