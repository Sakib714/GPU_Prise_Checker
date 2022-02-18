import requests
from bs4 import BeautifulSoup

doc = requests.get('https://www.ryanscomputers.com/gigabyte-geforce-gtx-1050-ti-d5-4g-4gb-gddr5-graphics-card')


code = BeautifulSoup(doc.content, 'html.parser')

special_prise = code.find_all(text="Special Price ")

price = special_prise[0].parent.find('span').contents[0].__str__()
# print(code.prettify())

print(price.replace(' ','').replace(',',''))