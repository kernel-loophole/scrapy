from cgitb import text
from bs4 import BeautifulSoup
from bs4 import CData
with open('index.html') as f:
    soup=BeautifulSoup(f)
   
    for i in soup.find_all('a'):
        print(i,i['href'])
    head_tag=soup.head
    for i in head_tag.children:
        print(i)
    for child in head_tag.descendants:
        print(child)
    for string in soup.strings:
        print(repr(string))
