#Extract latest jokes information
#Developed by Rahul Arora

import requests
from bs4 import BeautifulSoup
import random

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

ans = random.randrange(3)
if ans==0:
   ans = 1
websites = {1:'http://www.ajokeaday.com/ChisteAlAzar.asp?',2:'http://www.randomjoke.com/topic/oneliners.php'}
url = websites[ans]

def get():
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src)

   print "Knock Knock joke of the day :) \n"

   if ans==1:
      for info in ob.findAll('div',{'class':'chiste'}):
         joke = info.text.strip()
         joke = strip_non_ascii(joke)
         print joke + "\n"
         break

   else:
      ctr = 0
      for info in ob.findAll('p'):
         ctr = ctr+1
         if ctr==7:
            print info.text.strip() + "\n"
            break
         
   

