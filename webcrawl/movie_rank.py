from selenium import webdriver
from bs4 import BeautifulSoup

ctx = '../crawler/chromedriver'
driver = webdriver.Chrome(ctx)

driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source,'html.parser')
#print(soup.prettify())

all_tr = soup.find_all('tbody')
for i in all_tr:
    print(i.text)