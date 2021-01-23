import bs4
import requests
import re
from bs4 import BeautifulSoup
personal_url = 'https://www.kariyer.net/ozgecmis/ahmetcan81'
response = requests.get(personal_url)
html = response.content
soup = BeautifulSoup(html, "html.parser")
work_experinces = soup.find('div', class_="resume-edit--job-experience-info")
jobs = work_experinces.find_all('div', class_="resume-edit--job-experience")

for job in jobs:
    for item in job.find_all('span',{'class':['field-name','field-content','field-contentdate']}):
        print(item.text.strip())
    print("---------------------------------------")