#I analyzed the White House Briefings Statements (https://www.whitehouse.gov/briefings-statements/)
#the goal is to extract all the links that point to the briefings and statements
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, "html.parser")

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs["href"])

print(urls)
