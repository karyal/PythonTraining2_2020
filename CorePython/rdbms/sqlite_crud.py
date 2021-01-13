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

def select_all():
    str_sql ="""SELECT * FROM tbl_persons"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(str_sql)
        # rows = cursor.fetchone()# First Record
        rows = cursor.fetchall()
        for row in rows:
            print(row)# tuple
            print()
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def search_record(person_id):
    str_sql ="""SELECT * FROM tbl_persons WHERE person_id = ?"""
    values = (person_id, )
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        # rows = cursor.fetchone()# First Record
        rows = cursor.fetchall()
        for row in rows:
            print(row)# tuple
            print()
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def update_record(values):
    str_sql ="""UPDATE tbl_persons SET full_name=?, contact_address=? where person_id = ?"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        conn.commit()
        print("Update record successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def delete_record(values):
    str_sql = """DELETE FROM tbl_persons where person_id = ?"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        conn.commit()
        print("Delete Record Successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()