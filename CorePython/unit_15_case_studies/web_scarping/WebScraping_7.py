import requests
from bs4 import BeautifulSoup
source_url = 'https://risingnepaldaily.com/sports'
page = requests.get(source_url)
if page.status_code==200:
    print(page.content)
    soup = BeautifulSoup(page, "html.parser")
    print(soup.prettify())