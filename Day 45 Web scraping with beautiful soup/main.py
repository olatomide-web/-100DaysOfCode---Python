from bs4 import BeautifulSoup
import lxml
import requests

# #opening index.html as a file
# with open("index.html") as file:
#     content = file.read()

# soup = BeautifulSoup(content, 'lxml')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# #for finding ALL of a particular tag
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# heading_title = soup.find(name="h2", class_="title")
# print(heading_title)

# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "lxml")
# article_link = soup.find_all(class_="title", name="a")
# print(article_link)
# print(soup.title)
