import pandas as pd

data_bunsik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/분식/분식.csv')
data_ilsik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/일식/일식.csv')
data_jokbo = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/족발보쌈/족발보쌈.csv')
data_joongsik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/중식/중식.csv')
data_chicken = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/치킨/치킨.csv')
data_cafe = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/카페_디저트/카페_디저트.csv')
data_pizza = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/피자/피자.csv')
data_hansik = pd.read_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/한식/한식.csv')

df_bunsik = pd.DataFrame(data_hansik)
# df_ilsik = pd.DataFrame(data_ilsik)
# df_jokbo = pd.DataFrame(data_jokbo)
# df_joongsik = pd.DataFrame(data_joongsik)
# df_chicken = pd.DataFrame(data_chicken)
# df_cafe = pd.DataFrame(data_cafe)
# df_pizza = pd.DataFrame(data_pizza)
# df_hansik = pd.DataFrame(data_hansik)

df_bunsik = data_hansik.drop(['Unnamed: 0','아이디','날짜'], axis=1)
df_bunsik.drop_duplicates(inplace=True)
df_bunsik= df_bunsik[df_bunsik['맛평점'] != '-']
df_bunsik= df_bunsik[df_bunsik['양평점'] != '-']
df_bunsik= df_bunsik[df_bunsik['배달평점'] != '-']

df_bunsik['리뷰'] = df_bunsik['리뷰'].str.replace('\n', '')
df_bunsik['리뷰'] = df_bunsik['리뷰'].str.replace('"', '')
df_bunsik['리뷰'] = df_bunsik['리뷰'].str.replace('\r', '')

df_bunsik.replace({'맛평점': { '5': '맛2', '4': '맛1', '3': '맛1', '2': '맛0', '1': '맛0'}}, inplace=True)
df_bunsik.replace({'양평점': { '5': '양2', '4': '양1', '3': '양1', '2': '양0', '1': '양0'}}, inplace=True)
df_bunsik.replace({'배달평점': { '5': '배달2', '4': '배달1', '3': '배달1', '2': '배달0', '1': '배달0'}}, inplace=True)

df_bunsik['new_review'] = df_bunsik['맛평점'] + ' / ' + df_bunsik['양평점'] + ' / ' + df_bunsik['배달평점'] + ' / ' + df_bunsik['리뷰']
df_bunsik = df_bunsik['new_review']
df_bunsik.drop(columns='',inplace=True)
print(df_bunsik)

df_bunsik.to_csv('C:/Users/hufs0/OneDrive/바탕 화면/Project1/review_creator/음식/df_new/df_hansik_new.csv')