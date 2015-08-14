import os
import requests
from bs4 import BeautifulSoup
os.system("clear")

def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def SCRAPE():
    ctr = 0
    ans = 0
    temp = 0
    review = ""
    url = raw_input("Enter url : ")
    os.system("clear")
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)

    for find in ob.findAll('span',{'class':'review-text'}):
      review = find.text
      review = strip_non_ascii(review)
      review = review.strip()
      GETDATA(review)
      temp = RESULTS()
      ans = ans + temp
      ctr = ctr+1
      if ctr==10:
         if ans<0:
            print "Overall response : NEGATIVE" 
         elif ans>0:
            print "Overall response : POSITIVE" 
         else:
            print "Overall response : NEUTRAL" 
         break

def GETDATA(review):
   try:
      os.system("curl -d \"text=" + review + "\" http://text-processing.com/api/sentiment/ 2>/dev/null > result.txt")
   except:
      pass

def RESULTS():
   meaning = {'neg':'NEGATIVE','pos':'POSITIVE','ral':'NEUTRAL'}
   f = open("result.txt","r+")
   temp = f.readline()
   temp = temp[-5:-2]
   if meaning[temp]=="POSITIVE":
      return 1
   elif meaning[temp]=="NEGATIVE":
      return -1
   return 0
   f.close()

SCRAPE()

