from cgitb import text
from typing import final
import requests
from bs4 import BeautifulSoup
import json
def get_data():
    # start_url=BeautifulSoup('https://unsplash.com/')
    # data=requests.get('https://unsplash.com/')
    # x=data.json()
    # print(x)
    # html_file=BeautifulSoup(requests.get('https://unsplash.com/').json())
    
    x=requests.get('https://unsplash.com/')
    soup=x.json()
    final_str=soup
    print(final_str)
     
    
get_data()
    # return data.json()
# with open('un.html') as f:
#     x=get_data()
#     # f.write(x)
#     print(x)
# soup=BeautifulSoup(data.json())
# file=open("unspalsh.html",'a+')
# file.write(data.json())
# with open('unsplash.html') as f:
#     f.write(soup)
# for i in soup.find_all('a'):
#     print(i)