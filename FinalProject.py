import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab

# 시각화 할 때 한글 폰트를 사용하기 위한 설정
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

#-----------------------------------서울시 25개구 기상상황별 화재발생건수데이터 가공---------------------------------------

# 서울시 25개구 날씨상황별 화재발생건수 그래프를 그리기 위한 원본 데이터 (데이터 원본(2012~2018).csv)를 불러옴
df = pd.read_csv("데이터 원본(2012~2018).csv", index_col="구분", encoding="euc-kr")


# 맑음, 흐림, 눈, 비 4가지 경우만 나타내기 위해 필요없는 나머지 열속성들을 삭제
del df['합계']
del df['구름많음']
del df['구름조금']
del df['눈/비']
del df['비/눈']
del df['소나기']

# 합계 행 삭제
df = df.drop(['합계'])


# 데이터가 없으면 "-"로 표시해두어서 "-"를 0으로 바꿈
df['맑음'] = np.where(df['맑음'] == "-",0, df['맑음'])
df['흐림'] = np.where(df['흐림'] == "-",0, df['흐림'])
df['눈'] = np.where(df['눈'] == "-",0, df['눈'])
df['비'] = np.where(df['비'] == "-",0, df['비'])



# 기간(년도)별로 데이터 프레임을 저장
year_2016 = df['기간'] == 2016
year_2017 = df['기간'] == 2017
year_2018 = df['기간'] == 2018
df_2016 = df[year_2016]
df_2017 = df[year_2017]
df_2018 = df[year_2018]

# 기간 열 삭제
del df_2016['기간']
del df_2017['기간']
del df_2018['기간']

# 서울시 25개구 날씨상황별 화재발생건수를 년도별 csv파일로 저장
df_2016.to_csv('./기상상황별 화재발생 횟수2016 가공.csv', encoding="cp949", mode='w', index=True)
df_2017.to_csv('./기상상황별 화재발생 횟수2017 가공.csv', encoding="cp949", mode='w', index=True)
df_2018.to_csv('./기상상황별 화재발생 횟수2018 가공.csv', encoding="cp949", mode='w', index=True)

# 저장한 csv파일을 시각화하기 위해 불러옴
df_2016 = pd.read_csv('./기상상황별 화재발생 횟수2016 가공.csv', index_col="구분", encoding="euc-kr")
df_2017 = pd.read_csv('./기상상황별 화재발생 횟수2017 가공.csv', index_col="구분", encoding="euc-kr")
df_2018 = pd.read_csv('./기상상황별 화재발생 횟수2018 가공.csv', index_col="구분", encoding="euc-kr")

#---------------------------------서울시 25개구 기상상황별 화재발생건수데이터 시각화---------------------------------------

ax = df_2016.plot(kind="bar", title="기상상황별 화재발생 횟수", figsize=(20,5), legend=True, fontsize=12, rot=0)
ax.set_xlabel("구", fontsize=12)
ax.set_ylabel("2016", fontsize=12, rotation=0)
ax.legend(['맑음','구름많음','구름조금','흐림','눈'], fontsize=12)
plt.savefig("2016_서울시 25개구 기상상황별 화재발생건수.png")

ax = df_2017.plot(kind="bar", title="기상상황별 화재발생 횟수", figsize=(20,5), legend=True, fontsize=12, rot=0)
ax.set_xlabel("구", fontsize=12)
ax.set_ylabel("2017", fontsize=12, rotation=0)
ax.legend(['맑음','구름많음','구름조금','흐림','눈'], fontsize=12)
plt.savefig("2017_서울시 25개구 기상상황별 화재발생건수.png")

ax = df_2018.plot(kind="bar", title="기상상황별 화재발생 횟수", figsize=(20,5), legend=True, fontsize=12, rot=0)
ax.set_xlabel("구", fontsize=12)
ax.set_ylabel("2018", fontsize=12, rotation=0)
ax.legend(['맑음','흐림','눈','비'], fontsize=12)
plt.savefig("2018_서울시 25개구 기상상황별 화재발생건수.png")

plt.show()

#-----------------------------------년도별(2012~2018) 기상상활별 화재발생데이터 가공---------------------------------------

df2 = pd.read_csv("데이터 원본(2012~2018).csv", index_col="기간", encoding="euc-kr", thousands = ',')


# 맑음, 흐림, 눈, 비 4가지 경우만 나타내기 위해 필요없는 나머지 열속성들을 삭제
del df2['합계']
del df2['구름많음']
del df2['구름조금']
del df2['눈/비']
del df2['비/눈']
del df2['소나기']

# 합계 행만 필요하므로 년도별 합계만 뽑음
df2 = df2[df2.구분 == '합계']

# 년도별 합계파일을 csv로 저장
df2.to_csv('기상상황별 화재발생 합계.csv', encoding="cp949", mode='w', index=True)

# 저장한 csv파일을 시각화하기 위해 불러옴
df_total = pd.read_csv('기상상황별 화재발생 합계.csv', encoding="euc-kr")

# 구분 열 삭제
del df_total['구분']


# 기간(년도)를 기준으로 데이터를 오름차순 정렬
df_total = df_total.sort_values(by=['기간'],axis=0)


# 기상 상황 4가지 경우 별 데이터를 따로 저장
data_1 = df_total['맑음']
data_2 = df_total['흐림']
data_3 = df_total['눈']
data_4 = df_total['비']

# 년도 저장
data_year = df_total['기간']

sunny = []
gloomy = []
snow = []
rain = []
year = []

# 저장된 dataframe에서 데이터들을 int형식으로 변환 후 각 리스트에 저장 
for idx in range(len(data_year)):
    year.append(data_year[idx])
    sunny.append(int(data_1[idx]))
    gloomy.append(int(data_2[idx]))
    snow.append(int(data_3[idx]))
    rain.append(int(data_4[idx]))

#-----------------------------------년도별(2012~2018) 기상상활별 화재발생데이터 시각화---------------------------------------
fig = pylab.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)


# 맑음, 흐림, 눈, 비 4가지 그래프
ax.plot(year, sunny, marker="o")
ax.plot(year, gloomy, marker="v")
ax.plot(year, snow, marker="*")
ax.plot(year, rain, marker="D")

# x축, y축, 라벨 설정
ax.set_xlabel('년도')
ax.set_ylabel('발생 건수', rotation=0)
ax.set_xticks([2012, 2013, 2014, 2015, 2016,2017,2018])
ax.legend(['맑음', '흐림', '눈', '비'])

# 제목 설정
plt.title('년도별 기상상황별 화재발생 수 비교')

plt.savefig("(2012~2018)년도별 기상상황별 화재발생 수.png")

plt.show()

