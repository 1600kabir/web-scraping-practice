import requests
import bs4

site = requests.get('http://collegeboard.org')
soup = bs4.BeautifulSoup(site.text, 'lxml')
tag_select = soup.select('title')
print(tag_select)

