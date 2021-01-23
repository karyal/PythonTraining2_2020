import bs4
import requests
import re
from bs4 import BeautifulSoup
from datetime import timedelta
from datetime import datetime
import psycopg2
import sys
import pandas as pd

def connect(params_dic):
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    return conn
def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()
    #conn.close()
html = open('sample.html','r')
soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all('tr')
records = []
for row in rows:
    values = row.find_all('td')
    record = []
    for value in values:
        tmp_str = value.text.replace('\n','').strip()
        record.append(tmp_str)
    if len(record)>0:
        records.append(record.copy())
        record.clear()
#print(records)
new_records = []
for row in records:
    str_flight_time = datetime.strptime(row[4], '%H:%M:%S')
    str_arrival_time = datetime.strptime(row[5], '%H:%M:%S')
    diff = str_arrival_time - str_flight_time
    duration = diff.total_seconds() / 60 + diff.total_seconds() % 60
    row[6] = duration
    #print(duration)
    new_records.append(row.copy())
#print(new_records)
table_columns = ['Flight_From','Flight_To','Airlines','Flight_No','Flight_Time','Arrival_Time', 'Duration']
df1 = pd.DataFrame(new_records, columns=table_columns)
df1 = df1.drop(['Flight_No','Flight_Time','Arrival_Time'],1)
print(df1.head(3))
df1.to_csv('flights.csv',sep=';')

#Connection parameters
param_dic = {
    "host"      : "john.db.elephantsql.com",
    "database"  : "jssslfkj",
    "user"      : "jssslfkj",
    "password"  : "IgMQ6d4QzLNJ0Y0hhH_wld_XnLW3ox-1"
}
#Connect to the database
#conn = connect(param_dic)

for index, row in df1.iterrows():
    # print(row['Flight_From'], row['Flight_To'], row['Airlines'], row['Duration'])
    query = """INSERT into flights(Flight_From, Flight_To, Airlines, Duration) values('%s', %s, %s, %s);""" % (
    row['Flight_From'], "'" + row['Flight_To'] + "'", "'" + row['Airlines'] + "'", int(row['Duration']))
    print(query)
    #single_insert(conn, query)