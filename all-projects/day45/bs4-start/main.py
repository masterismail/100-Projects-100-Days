from bs4 import BeautifulSoup
import lxml 

with open("/home/tahseer/Desktop/python/100-Projects-100-Days/all-projects/day45/bs4-start/website.html") as file:
    content = file.read()


soup = BeautifulSoup(content,"html.parser")

all_anchor_tags = soup.find_all(name = "a")
print()

for tags in all_anchor_tags:
    print(tags.get("href"))