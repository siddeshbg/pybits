import bs4
from bs4 import BeautifulSoup
from urllib import urlopen

my_url="http://www.cricbuzz.com/"
client = urlopen(my_url)

html_page = client.read()
client.close()

soup = BeautifulSoup(html_page, "html.parser")

score_box = soup.findAll("div",{"class":"cb-col cb-col-25 cb-mtch-blk"})
print(score_box)
l = len(score_box)
print(l)

for i in range(l):
    print(score_box[i].a["title"])
    print(score_box[i].a.text)
    print()

'''
print(soup.prettify())
print("Title: %s" % soup.title)
print("Title String: %s" % soup.title.string)
print("Title Parent: %s" % soup.title.parent.name)
print("p: %s" % soup.p)
print("a (url): %s" % soup.a)
print(soup.find_all('a'))
print(soup.find(id="video_playlist"))

print("URLS found in this page")
for link in soup.find_all('a'):
    print(link.get('href'))

print("All text")
print("======================================")
print(soup.get_text())
'''