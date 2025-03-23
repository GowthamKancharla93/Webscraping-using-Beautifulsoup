import requests
import pandas 
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=i%20phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,"html.parser")
# print(soup)
names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in names[0:5]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
price=[]
for i in prices[0:5]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='XQDdHH')
rating=[]
for i in ratings[0:5]:
    d=i.get_text()
    rating.append(float(d))
# print(rating)

features=soup.find_all('ul',class_='G4BRas')
feature=[]
for i in features[0:5]:
    d=i.get_text()
    feature.append(d)
# print(feature)


images=soup.find_all('img',class_='DByuf4')
image=[]
for i in images[0:5]:
    d=i['src']
    image.append(d)
# print(img)

df=pandas.DataFrame()
data={'Names':name,'Prices':price,'Ratings':rating,'Features':feature,'Images':image}
df=pandas.DataFrame(data)
# print(df)
df.to_csv('Mobile_Data.csv')
print("Data Saved Successfully")

