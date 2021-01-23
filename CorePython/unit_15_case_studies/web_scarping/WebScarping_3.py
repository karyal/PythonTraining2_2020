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
print("Work Experinces")
for job in jobs:
    # Duration
    result31 = job.find('div', class_='experience-logo')
    result31_1 = result31.find('span', class_='experience')
    job_duration = result31_1.text.replace('\n', '')
    print("Duration : ",job_duration.strip())

    result33 = job.find('div', class_='experience-info')
    result33_1 = result33.find_all('div', class_='row')
    result33_1 = result33.find_all('div', class_ = re.compile('^fields col-.*'))
    i = 0
    while(i<len(result33_1)):
        value1 = result33_1[i].find('span', class_="field-name")
        value2 = result33_1[i].find('span', class_ = re.compile('^field-content.*'))
        if value1!=None and value2!=None:
            print(value1.text.strip(), " : ",value2.text.strip())
        i+=1
    print("-------------------------------------------------------------")