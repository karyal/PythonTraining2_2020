import requests # pip install requests
from bs4 import BeautifulSoup
persons=[]
print(len(persons))
def get_personal_details(url):
    personal_url = url
    response = requests.get(personal_url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    full_name = 'NA'
    title = 'NA'
    summary = 'NA'
    summary_body = 'NA'
    full_name = soup.find(class_="candidate-name")
    title = soup.find(class_="candidate-job")
    summary = soup.find(class_="resume-edit--summary-info")
    summary_body = summary.find(class_="content-body")
    txt_fn = 'NA'
    txt_dg = 'NA'
    txt_su = 'NA'
    if full_name != None:
        txt_fn = full_name.text
    if title != None:
        txt_dg = title.text
    if summary_body != None:
        txt_su = summary_body.text
        txt_su = txt_su.replace('\n', '')
        print(txt_su)
    person = [txt_fn, txt_dg, txt_su]
    persons.append(person)

all_links =['https://www.kariyer.net/ozgecmis/cemokcu', 'https://www.kariyer.net/ozgecmis/cemokcu', 'https://www.kariyer.net/ozgecmis/ebrarkul', 'https://www.kariyer.net/ozgecmis/ebrarerdogan', 'https://www.kariyer.net/ozgecmis/esradurukan', 'https://www.kariyer.net/ozgecmis/alibalball', 'https://www.kariyer.net/ozgecmis/omercevik1484', 'https://www.kariyer.net/ozgecmis/omerbaylan', 'https://www.kariyer.net/ozgecmis/enesmalikgulcan', 'https://www.kariyer.net/ozgecmis/ahmetenesakosman', 'https://www.kariyer.net/ozgecmis/tahaerol', 'https://www.kariyer.net/ozgecmis/baris3408', 'https://www.kariyer.net/ozgecmis/asudezeynepdaniscv', 'https://www.kariyer.net/ozgecmis/mervegezer', 'https://www.kariyer.net/ozgecmis/mervegulener', 'https://www.kariyer.net/ozgecmis/busraayarr', 'https://www.kariyer.net/ozgecmis/busrabalci34', 'https://www.kariyer.net/ozgecmis/muhammedyalcinatlikan', 'https://www.kariyer.net/ozgecmis/muhammetdemirkoparan', 'https://www.kariyer.net/ozgecmis/ozgecmis', 'https://www.kariyer.net/ozgecmis/kubraakyol', 'https://www.kariyer.net/ozgecmis/fadimetugceerdem', 'https://www.kariyer.net/ozgecmis/tugcekya', 'https://www.kariyer.net/ozgecmis/iremyucekaya', 'https://www.kariyer.net/ozgecmis/iremonay', 'https://www.kariyer.net/ozgecmis/rumeysapeker', 'https://www.kariyer.net/ozgecmis/rumeysacengiz', 'https://www.kariyer.net/ozgecmis/beyza.gungor', 'https://www.kariyer.net/ozgecmis/ahmetcan81', 'https://www.kariyer.net/ozgecmis/ahmetozdemir813453', 'https://www.kariyer.net/ozgecmis/elifyildirim063', 'https://www.kariyer.net/ozgecmis/elifdobrucali', 'https://www.kariyer.net/ozgecmis/omerbatuhankizilisik', 'https://www.kariyer.net/ozgecmis/omerfarukozyurt1', 'https://www.kariyer.net/ozgecmis/enescamuzcu', 'https://www.kariyer.net/ozgecmis/alpererdogan38', 'https://www.kariyer.net/ozgecmis/alpercapkin', 'https://www.kariyer.net/ozgecmis/ahmetyolalaner', 'https://www.kariyer.net/ozgecmis/ahmeddemirezen', 'https://www.kariyer.net/ozgecmis/elifffatarrr', 'https://www.kariyer.net/ozgecmis/elifgulsu', 'https://www.kariyer.net/ozgecmis/cemokcu', 'https://www.kariyer.net/ozgecmis/cemokcu', 'https://www.kariyer.net/ozgecmis/ebrarkul', 'https://www.kariyer.net/ozgecmis/ebrarerdogan', 'https://www.kariyer.net/ozgecmis/esradurukan', 'https://www.kariyer.net/ozgecmis/alibalball', 'https://www.kariyer.net/ozgecmis/omercevik1484', 'https://www.kariyer.net/ozgecmis/omerbaylan', 'https://www.kariyer.net/ozgecmis/enesmalikgulcan', 'https://www.kariyer.net/ozgecmis/ahmetenesakosman', 'https://www.kariyer.net/ozgecmis/tahaerol', 'https://www.kariyer.net/ozgecmis/baris3408', 'https://www.kariyer.net/ozgecmis/asudezeynepdaniscv', 'https://www.kariyer.net/ozgecmis/mervegezer', 'https://www.kariyer.net/ozgecmis/mervegulener', 'https://www.kariyer.net/ozgecmis/busraayarr', 'https://www.kariyer.net/ozgecmis/busrabalci34', 'https://www.kariyer.net/ozgecmis/muhammedyalcinatlikan', 'https://www.kariyer.net/ozgecmis/muhammetdemirkoparan', 'https://www.kariyer.net/ozgecmis/ozgecmis', 'https://www.kariyer.net/ozgecmis/kubraakyol', 'https://www.kariyer.net/ozgecmis/fadimetugceerdem', 'https://www.kariyer.net/ozgecmis/tugcekya', 'https://www.kariyer.net/ozgecmis/iremyucekaya', 'https://www.kariyer.net/ozgecmis/iremonay', 'https://www.kariyer.net/ozgecmis/rumeysapeker', 'https://www.kariyer.net/ozgecmis/rumeysacengiz', 'https://www.kariyer.net/ozgecmis/beyza.gungor', 'https://www.kariyer.net/ozgecmis/ahmetcan81', 'https://www.kariyer.net/ozgecmis/ahmetozdemir813453', 'https://www.kariyer.net/ozgecmis/elifyildirim063', 'https://www.kariyer.net/ozgecmis/elifdobrucali', 'https://www.kariyer.net/ozgecmis/omerbatuhankizilisik', 'https://www.kariyer.net/ozgecmis/omerfarukozyurt1', 'https://www.kariyer.net/ozgecmis/enescamuzcu', 'https://www.kariyer.net/ozgecmis/alpererdogan38', 'https://www.kariyer.net/ozgecmis/alpercapkin', 'https://www.kariyer.net/ozgecmis/ahmetyolalaner', 'https://www.kariyer.net/ozgecmis/ahmeddemirezen', 'https://www.kariyer.net/ozgecmis/elifffatarrr', 'https://www.kariyer.net/ozgecmis/elifgulsu']

for link in all_links:
    get_personal_details(link)
    break