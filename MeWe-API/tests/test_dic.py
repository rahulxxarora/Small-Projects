import requests
from bs4 import BeautifulSoup
import re

flag = 0

def display(query):
    url = "http://www.merriam-webster.com/dictionary/"
    url = url + query
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)

    for info in ob.findAll('div',{'class':'ld_on_collegiate'}):
        word = info.text
        word = word.split(':')
        for i in word:
            if i.strip():
                flag = 1
                print "-> " + i.strip()

    if flag==0:
        print "-> No result found"


def get(query):
    url = "http://www.merriam-webster.com/dictionary/"
    url = url + query
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)

    results = []
    for info in ob.findAll('div',{'class':'ld_on_collegiate'}):
        word = info.text
        word = word.split(':')
        for i in word:
            if i.strip():
                flag = 1
                results.append(i.strip())

    if flag==0:
        results.append("No result found")
    return results

display('elephant')
ans = get('elephant')
print ans
