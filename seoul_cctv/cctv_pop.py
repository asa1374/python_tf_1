import pandas as pd
import numpy as np
import folium

ctx = '../data/'
pop = ctx + 'population_in_Seoul.xls'
csv = ctx + 'CCTV_in_Seoul.csv'

df_pop = pd.read_excel(pop
                         ,encoding='utf-8'
                         ,header=2
                         ,usecols='B,D,G,J,N')

df_cctv = pd.read_csv(csv)

df_cctv_col = df_cctv.columns
df_pop_col = df_pop.columns

"""
df_cctv_col
['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년']

df_pop_col
['구별', '인구수', '한국인', '외국인', '고령자']
"""

df_cctv.rename(columns={df_cctv.columns[0]:'구별'},inplace=True)

df_pop.rename(columns={df_pop.columns[0]:'구별'
                         ,df_pop.columns[1]:'인구수'
                         ,df_pop.columns[2]:'한국인'
                         ,df_pop.columns[3]:'외국인'
                         ,df_pop.columns[4]:'고령자'}
                ,inplace=True)
"""
문제1 df_cctv 를 소계기준 오름차순 정렬
문제2 df_pop 에서 0번행 삭제
문제3 df_pop 에서 구별 기준 중복제거
문제4 df_pop 에서 null 체크 (null 있는지 여부)
문제5 df_pop 에서 인구수 기준 오름차순 정렬
문제6 df_cctv 에서 '2013년도 이전', '2014년', '2015년', '2016년'
"""

df_cctv.sort_values(by='소계',ascending=True) #ex1
df_pop.drop(index=0,inplace=True)                    #ex2
df_pop.groupby(['구별']).sum()          #ex3
df_pop.drop(index=26,inplace=True)
df_pop[df_pop['구별'].isnull()]         #ex4
df_pop.sort_values(by='인구수',ascending=True) #ex5
df_cctv.drop(['2013년도 이전','2014년','2015년','2016년'],1,inplace=True) #ex6
df_pop['외국인비율'] = (df_pop['외국인'] / df_pop['인구수']) * 100
df_pop['고령자비율'] = (df_pop['고령자'] / df_pop['인구수']) * 100

df_cctv_pop = pd.merge(df_cctv,df_pop,on='구별')

df_cctv_pop.set_index('구별',inplace=True)

"""
r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
"""
cor1 = np.corrcoef(df_cctv_pop['고령자비율'],df_cctv_pop['소계'])
cor2 = np.corrcoef(df_cctv_pop['외국인비율'],df_cctv_pop['소계'])

# print("고령자비율 상관계수 {}, 외국인비율 상관계수 {}".format(cor1,cor2))

df_cctv_pop.to_csv(ctx+'df_cctv_pop')







