from distutils.filelist import findall
from bs4 import BeautifulSoup 
html_doc='''<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names
were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>'''
soup=BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())
# soup_title=soup.title()
print("title====>",soup.title)
print("name=====>",soup.title.name)
print("string====>",soup.title.string)
#find all a tags
print('=====>',soup.find_all('a'))
for i in soup.find_all('a'):
    print(i['href'])
for j in soup.find_all('p'):
    print(j)
print(soup.find(id='link2'))
print(soup.get_text())