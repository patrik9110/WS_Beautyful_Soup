#I analyzed the Google english homepage and I went through some of the Beautiful Soup and Request modules basic fundaments.
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/?hl=en")
print(result.status_code)
#print(result.headers)
src = result.content
soup = BeautifulSoup(src, "html.parser")
links = soup.find_all("a")
#print(links)
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs["href"])
