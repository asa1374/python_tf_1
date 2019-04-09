from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

kospi_now = soup.select('#KOSPI_now')

print("시간의 코스피 지수는")
for i in kospi_now:
    print(i.text)

time1 = soup.select('#time1')

for i in time1:
    print(i.text.lstrip())
