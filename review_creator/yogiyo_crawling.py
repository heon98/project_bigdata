import time
import pandas as pd
import numpy as np
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.yogiyo.co.kr/mobile/#/286059/'
# response = requests.get(url)
# response.raise_for_status()
# soup = BeautifulSoup(response.text, "lxml")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
button = driver.find_element(By.CSS_SELECTOR, '#content > div.restaurant-detail.row.ng-scope > div.col-sm-8 > ul > li:nth-child(2)')
#button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/ul/li[2]/a')
time.sleep(3)
#button.send_keys(Keys.ENTER)
button.click()
time.sleep(3)
df = pd.DataFrame(columns=["아이디", "날짜", "맛평점", "양평점", "배달평점", "리뷰"])
#df = pd.DataFrame(columns=["아이디", "날짜", "평점", "리뷰"])


more_button = driver.find_element(By.XPATH, '//*[@id="review"]/li[12]/a')
SCROLL_PAUSE_TIME = 3
cnt = 0
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")        

while True:
  # Scroll down to bottom                                                      
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  # Wait to load page
  time.sleep(SCROLL_PAUSE_TIME) 
  more_button.click()    
  print('click')                                         
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  
  time.sleep(SCROLL_PAUSE_TIME)
  cnt += 1
  if cnt == 259:
    break
  # Calculate new scroll height and compare with last scroll height           
  new_height = driver.execute_script("return document.body.scrollHeight")

  if new_height == last_height:                                                
    break

  last_height = new_height

html = driver.page_source

html = BeautifulSoup(html, 'html.parser')
review_box = html.find_all("li", class_= "list-group-item star-point ng-scope")

for review in review_box:
  # ID
  try:
    userID = review.find("span", class_="review-id ng-binding").text
    print(userID)
  except:
    userID = '-'  
  
  # 날짜
  try:
    date = review.find("span", class_="review-time ng-binding").text
    print(date)
  except:
    date = '-'   
  # review_box = html.find_all("li", class_= "list-group-item star-point ng-scope")
  # 평점
  try:
    stars = review.find_all("span", class_ = "points ng-binding")
    taste, quantity, delivery = stars[0].text, stars[1].text, stars[2].text
    #avg_star = (float(taste)+float(quantity)+float(delivery)) / 3
    #s = []
    #for star in stars:
     # s.append(float(star))
      #print(star.text)
      
    #stars = review.find_all("span", class_="points ng-binding")
    
    #for star in stars:
     # taste = star.text
      #quantity = star.text
      #delivery = star.text
      #avg_star =(taste+quantity+delivery)/3
      #print(taste + quantity + avg_star)
  except:
    taste = '-'
    quantity = '-'
    delivery = '-'
    avg_star = '-'
    
  # 리뷰
  try:
    comment = review.find("p", class_="ng-binding").text
    print(comment)
  except:
    comment = '-' 


  data = {'아이디': userID, '날짜': date, '맛평점': taste,  '양평점' : quantity,
                '배달평점': delivery, '리뷰': comment}
  #data = {'아이디': userID, '날짜': date, '평점': s, '리뷰': comment}

  df = df.append(data, ignore_index=True)
  time.sleep(1)


df.to_csv('2600_소풍닭강정_본점.csv', encoding="utf-8-sig")
print(df)
#print(review.find("span", class_= "points ng-binding").text)