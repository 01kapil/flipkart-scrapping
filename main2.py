import requests
import pandas as pd
from bs4 import BeautifulSoup



description = []
ratings = []
mobile_name= []
Price = []

for page in range(1,23):

    url = f"https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page={page}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")


    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

   # print(box)
    names= box.find_all("div",class_="_4rR01T")
    for i in names:
         name=i.text
         mobile_name.append(name)

   # print(mobile_name)

    rating = box.find_all("div", class_="_3LWZlK")
    for i in rating:
         name=i.text
         ratings.append(name)
   # print(ratings)

    descri = box.find_all("ul", class_="_1xgFaf")
    for i in descri:
         name=i.text
         description.append(name)
   # print(description)

    price = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in price:
        name = i.text
        Price.append(name)

   # print(Price)


data= {'MOBILE_NAMES':mobile_name,
       'PRICE':Price,
       'DESCRIPTION':description}



df =pd.DataFrame(data)
df.to_csv("Samsung_Mobile-phones-On_flipkart.CSV")

