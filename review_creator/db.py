import pandas as pd

df_bunsik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_bunsik_new.csv', encoding = 'utf-8')
# df_cafe = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_cafe_new.csv')
# df_chcken = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_chcken_new.csv')
# df_hansik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_hansik_new.csv')
# df_ilsik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_ilsik_new.csv')
# df_jokbo = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_jokbo_new.csv')
# df_joongsik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_joongsik_new.csv')
# df_pizza = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_pizza_new.csv')

import pymysql
import csv
feature = 'bunsik'

conn = pymysql.connect(host='localhost', user='root', passwd='jw1130!@#~',
                       db='food', charset='utf8')

cur = conn.cursor()

sql = '''CREATE TABLE bunsik(
  index int(10),
  new_review VARCHAR(600)
)
'''
cur.execute(sql)

