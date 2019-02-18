#An introduction to Beautiful Soup objects
import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

#with open("index.html", "w") as f:
#    f.write(html_doc)

soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify())
#print(soup.title)
#print(soup.find("title"))
#print(soup.find_all("b"))

#tag = soup.b
#tag.name = "blockquote"
#print(tag)

#tag = soup.find_all("b")[2]
#print(tag)
#print(tag["id"])

#tag = soup.find_all("b")[3]
#print(tag.attrs)

#tag = soup.find_all("b")[3]
#print(tag)
#tag["another-attribute"] = 2
#print(tag)

#tag = soup.find_all("b")[3]
#print(tag)                      the complete tag
#del tag["id"]                   erase the "id" atribute
#print(tag)                      the tag without the "id" atribute
#del tag["another-attribute"]    erase the "another-atribute" atribute
#print(tag)                      the tag without any atributes

#tag = soup.find_all("b")[3]
#print(tag)
#print(tag.string)
#tag.string.replace_with("This is another string")
#print(tag)
#print(tag.string)
