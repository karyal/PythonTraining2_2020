import sqlite3
import sys

DB_FILE = 'mydb.db'

def connect():
    try:
        conn = sqlite3.connect(DB_FILE)
        print("Connect sqlite database successfully")
    except:
        print("Error", sys.exc_info()[1])
    finally:
        conn.close()

def create_table_person():
    # Data Definition Language (DDL)
    str_sql = """
        CREATE TABLE IF NOT EXISTS tbl_persons(
            person_id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            contact_address TEXT NOT NULL 
        );
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(str_sql)
        conn.commit()# Saved Change
        print("Create table successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def insert_record(values):
    str_sql="""INSERT INTO tbl_persons(person_id, full_name, contact_address) values(?, ?, ?)"""
    #values = (1, 'Krishna Aryal','Balaju, Ktm')
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        conn.commit()# Save Change
        print("Insert record on table successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()