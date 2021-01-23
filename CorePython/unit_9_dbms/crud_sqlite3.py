import sqlite3
from sqlite3 import Error
import sys

DB_FILE = 'mydb.db'

def connect1():
    try:
        conn = sqlite3.connect(DB_FILE)
        print(sqlite3.version)
        print("Connect database successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        conn.close()

def create_table1():
    sql="""
        CREATE TABLE IF NOT EXISTS tbl_person(
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            contact_address TEXT NOT NULL
        );
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Create table successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

def insert_record1():
    sql="""INSERT INTO tbl_person(id, full_name, contact_address) values(?, ?, ?)"""
    values = (1, 'Krishna Aryal','Kathmandu')
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        print("Insert record successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

def select_record1():
    sql="""SELECT * FROM tbl_person"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

def update_record():
    sql="""UPDATE tbl_person set full_name=?, contact_address=? where id =?"""
    values=('New Name','New Address',1)
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        print("Record update successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

def delete_record():
    sql="""DELETE from tbl_person where id =?"""
    values=(1, )
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        print("Record delete successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

# connect1()
#create_table1()
#insert_record1()
#update_record()
#delete_record()
#select_record1()
