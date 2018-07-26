from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
nytimes_html = r.text

soup = BeautifulSoup(nytimes_html, 'html.parser')

article_titles = []

for title in soup.find_all("article", class_='story theme-summary'):
    try:
        if title.h2.a.string is not None:
            article_titles.append(title.h2.a.string)
    except AttributeError:
        continue

print("\n\n".join(article_titles))
print("\n\n\n\n\n\n")




#print("\n\n".join(article_titles))
