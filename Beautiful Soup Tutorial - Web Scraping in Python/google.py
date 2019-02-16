#En este script analizo el sitio web de google.com en Ingles
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
