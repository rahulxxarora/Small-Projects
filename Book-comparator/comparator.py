from threading import Thread
import requests
from bs4 import BeautifulSoup

word = raw_input('Enter name : ')

def strip_non_ascii(string):
   stripped = (c for c in string if 0 < ord(c) < 127)
   return ''.join(stripped)

def Thread1():
   url = "http://www.amazon.in/s/ref=nb_sb_noss/276-0458272-7880320?url=search-alias%3Daps&field-keywords=" + str(word)
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src, 'lxml')

   for find in ob.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
      price = find.text
      print "AMAZON",
      print price.strip().split('.')[0]
      break

def Thread2():
   url = "http://www.infibeam.com/search?q=" + str(word)
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src, 'lxml')
   
   for find in ob.findAll('span',{'class':'final-price'}):
      price = find.text
      price = price.replace('Rs.','')
      print "INFIBEAM",
      print price.strip()
      break

def Thread3():
   flag=0
   url = "http://www.flipkart.com/search?q=" + str(word) + "&as=off&as-show=on&otracker=start"
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src, 'lxml')

   for find,find2 in zip(ob.findAll('a',{'class':'lu-title'}),ob.findAll('div',{'class':'pu-final fk-font-17 fk-bold'})):
      if flag==0:
         flag=1
      title = find.text
      price = find2.text
      price = price.replace('Rs.','')
      print "FLIPKART",
      print price.strip()
      break
      
   if flag!=1:
      for temp,temp2 in zip(ob.findAll('div',{'class':'pu-final'}),ob.findAll('a',{'class':'fk-display-block'})): 
         price = temp.text
         title = temp2.text
         price = price.replace('Rs.','')
         print "FLIPKART",
         print price.strip()   
         break

def Thread4():
   url = "http://www.bookadda.com/general-search?searchkey=" + str(word)
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src, 'lxml')

   for find in ob.findAll('span',{'class':'new_price'}):
      price = find.text
      price = price.replace('Rs.','')
      break
   
   print "BOOKADDA", 
   print price.strip()

def Thread5():
   flag=0
   url = "http://www.junglee.com/mn/search/junglee/ref=nav_sb_gw_noss?field-keywords=" + str(word) + "&rush=g&url=search-alias%3Daps"
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src, 'lxml')

   for find in ob.findAll('span',{'class':'price'}):
      price = find.text
      price = strip_non_ascii(price)
      print "JUNGLEE",
      print price.strip().split('.')[0]
      break
   

Thread(target=Thread1, args=()).start()
Thread(target=Thread2, args=()).start()
Thread(target=Thread3, args=()).start()
Thread(target=Thread4, args=()).start()
Thread(target=Thread5, args=()).start()




