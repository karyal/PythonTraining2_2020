import json
import requests

api_url = 'http://localhost:8000/customers/'

def get(id):
    response = requests.get(api_url+str(id))
    if response.status_code==200:
        record = json.loads(response.content)
        return record
    else:
        return None

def get_all():
    response = requests.get(api_url)
    if response.status_code==200:
        records = json.loads(response.content)
        return records
    else:
        return None

def insert_record(record):
    response = requests.post(api_url, json=record)
    if response.status_code==200:
        return True
    else:
        return False

def update_record(record):
    tmp_api_url = api_url+str(record['id'])+'/'
    response = requests.put(tmp_api_url, json=record)

def delete_record(id):
    tmp_api_url = api_url+str(id)+'/'
    response = requests.delete(tmp_api_url)
    if response.status_code==204:
        return True
    else:
        return False

# Record Insert
record = {'id':0, 'fullname':'Raj Rai','address':'Balaju, KTM'}
insert_record(record)

# Record Search
record = get(10)
if record!=None:
    print(record)
else:
    print("Record not found")

# Record Update
record = {'id':8, 'fullname':'Raj Sharma','address':'Kalanki, KTM'}
update_record(record)

# Record Delete
# print(delete_record(9))

# Get All Records
persons = get_all()
print(persons)