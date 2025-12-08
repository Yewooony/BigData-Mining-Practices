import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.rc('font', family ='Malgun Gothic')

df = pd.read_csv('age.csv', encoding='cp949', index_col = 0)
df = df.div(df['총인구수'], axis = 0)     
del df['총인구수'], df['연령구간인구수']  

name = input('원하는 지역의 이름을 입력해주세요 : ') 
a = df.index.str.contains(name) 
df2 = df[a]
x = df.sub(df2.iloc[0], axis = 1)
y = np.power(x, 2)
z = y.sum(axis = 1)
i = z.sort_values().index[:5]
df.loc[i].T.plot()
plt.show()
