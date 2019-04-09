import pandas as pd
import folium

ctx = '../data/'
pop = ctx + 'population_in_Seoul.xls'
csv = ctx + 'CCTV_in_Seoul.csv'


popdata = pd.read_excel(pop)
print(popdata.head())

cctvdata = pd.read_csv(csv)
print(cctvdata.head())
