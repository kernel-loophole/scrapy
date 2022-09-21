from bs4 import BeautifulSoup
with open('index.html') as f:
    soup=BeautifulSoup(f)
# tages=soup.p
# print(type(tages))