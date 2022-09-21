from bs4 import BeautifulSoup
with open('index.html') as f:
    soup=BeautifulSoup(f)
tages=soup.p
tages.name="test"
try:
    print(tages['id'])
except:
    print("error")
del tages