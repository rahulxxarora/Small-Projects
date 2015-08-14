#Extract flipkart products
#Developed by Rahul Arora

import requests
from bs4 import BeautifulSoup
import os

def check(k):
    flag=0
    ctr=0
    url = "http://www.flipkart.com/search?q=" + str(k) + "&as=off&as-show=on&otracker=start"
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)

    for find,find2 in zip(ob.findAll('a',{'class':'lu-title'}),ob.findAll('div',{'class':'pu-final fk-font-17 fk-bold'})):
      if flag==0:
         print("Top ten products are :\n")
         flag=1
      title = find.text
      price = find2.text
      price = price.replace('Rs.','Rupees')
      print(title.strip() + " " + price.strip())
      ctr += 1
      if ctr==10:
         break
      
    if flag!=1:
      print("Exact match not found") 
      print("Similar Top three products are :\n")
      for temp,temp2 in zip(ob.findAll('div',{'class':'pu-final'}),ob.findAll('a',{'class':'fk-display-block'})): 
         price = temp.text
         title = temp2.text
         price = price.replace('Rs.','Rupees')
         print(title.strip() + " " + price.strip())
         ctr += 1
         if ctr==3:
            break

word = raw_input("Enter product : ")
check(word)
