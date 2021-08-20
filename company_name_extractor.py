import requests
from bs4 import BeautifulSoup

URL = 'http://textilefashionstudy.com/list-of-textile-industries-in-india-textile-products-manufacturer/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

comp_list = soup.find_all('li')


with open("doc.txt", "w+") as doc_file:
    for comp in comp_list:
        if ("Ltd" or "Limited") in comp.text and len(comp.text) < 60:
            doc_file.write(comp.text + "\n")
