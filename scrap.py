from bs4 import BeautifulSoup
import requests
import html5lib
url = "https://codewithharry.com"

#step 1: get the html
r  = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#step 2: parse the html
soup = BeautifulSoup(htmlContent  , 'html.parser')
print(soup)

#step 3: html tree traversal
#commanly used types of objects:
#1. tag
#2. navigablesoup
#3 . beautifulsoup
#4. comment

title = soup.title # get the title of html page
print(type(soup))
print(type(title))
print(type(title.string))

#get all paragraph from page
paras = soup.find_all('p')
print(paras)

#get all anchors tags from the page
anc = soup.find_all('a')
print(anc)

#get first element in html page
print(soup.find('p'))

#get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#get all the links on the page
anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href')!= "#"):

        linktext = "https://codewithharry.com"+link.get('href')
        all_links.add(link)
        print(linktext)
       # print(all_links)

navbarSupportedContent = soup.find(id ="navbarSupportedContent")
# .contents - a tag's children are available as a generator( info stored in memory to acess)
# .children - a tag's children are available as a genrator(info is not in actual memory but u can acess)

for x in navbarSupportedContent.contents:
    print(x)

for y in navbarSupportedContent.stripped_strings:
    print(y)

for item in navbarSupportedContent.parents:
    print(item.name)


