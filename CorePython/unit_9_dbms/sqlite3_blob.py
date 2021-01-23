import os
import sys
import sqlite3
from sqlite3 import Error

DB_FILE = 'mydb.db'

def create_or_open_db():
    db_is_new = not os.path.exists(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    if db_is_new:
        sql = '''
        create table if not exists PICTURES(
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          PICTURE BLOB,
          TYPE TEXT,
          FILE_NAME TEXT);
        '''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
        conn.close()
        print('Database Schema Create Successfully\n')
    else:
        print('Database Schema Already Exists\n')
    return conn


def create_db_table():
    try:
        db_is_new = not os.path.exists(DB_FILE)
        conn = sqlite3.connect(DB_FILE)
        sql = '''
          create table if not exists tbl_photos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PICTURE BLOB,
            TYPE TEXT,
            FILE_NAME TEXT);
        '''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
        conn.commit()
        conn.close()
        print("Table create successfully")
    except:
        print("Error : "+sys.exc_info()[1])


def insert_picture(picture_file):
    try:
        conn = sqlite3.connect(DB_FILE)
        with open(picture_file, 'rb') as input_file:
            ablob = input_file.read()
            base=os.path.basename(picture_file)
            afile, ext = os.path.splitext(base)
            sql = '''INSERT INTO PICTURES(PICTURE, TYPE, FILE_NAME) VALUES(?, ?, ?);'''
            conn.execute(sql,[sqlite3.Binary(ablob), ext, afile])
            conn.commit()
            conn.close()
            print("Insert record sucessfully")
    except:
        print("Error : "+sys.exc_info()[1])

def update_picture(id, picture_file):
    try:
        conn = sqlite3.connect(DB_FILE)
        with open(picture_file, 'rb') as input_file:
            ablob = input_file.read()
            base=os.path.basename(picture_file)
            afile, ext = os.path.splitext(base)
            sql = '''UPDATE PICTURES SET PICTURE=?, TYPE=?, FILE_NAME=? WHERE ID=?;'''
            conn.execute(sql,[sqlite3.Binary(ablob), ext, afile, id])
            conn.commit()
            conn.close()
            print("Update record sucessfully")
    except:
        print("Error : "+sys.exc_info()[1])

def select_picture(id):
    try:
        sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id"
        param = {'id': id}
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql, param)
        ablob, ext, afile = cursor.fetchone()
        filename = str(id)+"_"+afile + ext
        with open(filename, 'wb') as output_file:
            output_file.write(ablob)
        print("Select and create image file sucessfully")
        return filename
    except Error:
        print("Error  : "+sys.exc_info()[1])

#create_or_open_db()
#create_db_table()
#insert_picture("image1.png")
update_picture(1, "image01.png")

file_name = select_picture(1)
print(file_name)

# References.txt
# http://www.numericalexpert.com/blog/sqlite_blob_time/