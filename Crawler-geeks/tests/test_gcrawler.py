#Developed by Rahul Arora
from bs4 import BeautifulSoup
import requests
import re

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

visited = []
new = []
new.append("http://www.geeksforgeeks.org/category/interview-experiences/")

def gcrawl(query):
   while True:
      if not new:
         break 
      url = new.pop() 
      if url in visited:
         continue
      else:
         visited.append(url)
      page = requests.get(url)
      src = page.text
      ob = BeautifulSoup(src)
      try:
         for find in ob.findAll('a',href=True):
            temp = find.string
            ans = re.search(query,temp,re.IGNORECASE)
            if ans and find.get('href') not in visited:
               temp = strip_non_ascii(temp)
               print temp + "\n"
               print find.get('href') + "\n"
               visited.append(find.get('href'))
            else:
               link = find.get('href')
               ans = re.search('page/',link)
               if ans:
                  if link not in visited:
                     new.append(link)
      except:
         pass

gcrawl("Microsoft") #Test query
