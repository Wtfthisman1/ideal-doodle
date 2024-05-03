import pandas as pd
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString

url = 'https://pogoda.mail.ru/country/russia/'
soup = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text, 'html.parser')
cities = soup.find_all('span', class_='city-list__val city-list__val-text')
temperature = soup.find_all('span', class_='city-list__val city-list__val-temperature')

#Создадим датафрейм из двух столбцов и заполним его полученными значениями
df = pd.DataFrame({'city': cities,
                  'temperature': temperature})

df['city'] = df['city'].apply(lambda x: x.text.strip())
df['temperature'] = df['temperature'].apply(lambda x: int(x.text.strip()[:-1]))
print(df [['city', 'temperature']])
t_max = df['temperature'].max()
df_max = df[df['temperature'] == t_max]
print(df_max)
#В этой строке мы выведем все города, в которых максимальная температура
print('Теплее всего сейчас в: '+ ', '.join(df_max['city'].values))


#df=df[1]
#print(df.info())
#print(df.min())
#print(df['Золото руб./грамм'].min())
#print(df["Золото руб./грамм"].max())
#gold_min = df['Золото руб./грамм'].min()
#gold_max = df['Золото руб./грамм'].max()
#count_gold = 100000 / gold_min
#money_gold = count_gold * gold_max
#print(money_gold)
#money = money_gold - 100000
#print(money)
