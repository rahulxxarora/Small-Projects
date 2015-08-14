#MEWE

Unofficial API to get search word meanings on official website of Merriam-Webster.

#REQUIREMENTS

BeautifulSoup and requests

#EXAMPLE
   
   from mewe import dic

   dic.display('elephant')

   ans = dic.get('elephant')
