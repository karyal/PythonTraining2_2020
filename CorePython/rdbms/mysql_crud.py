# pip install mysql-connector
import mysql.connector
import sys

def connect_server():
    #conn = None
    try:
        # Connect with database server
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        conn.close()
        print("Connect with database server successfully")
    except:
        print("Error : ", sys.exc_info())
    finally:
        pass

def connect_dbms():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='python2')
        conn.close()
        print("Connect with database server successfully")
    except:
        print("Error : ", sys.exc_info())
    finally:
        pass

def insert_record(values):
    str_sql = """INSERT INTO contacts(full_name, contact_address, email_address) values(%s, %s, %s)"""
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='python2')
        if conn.is_connected():
            cursor=conn.cursor()
            cursor.execute(str_sql, values)
            conn.commit()
            print("Save record successfully")
    except:
        print("Error : ", sys.exc_info())
    finally:
        pass

# Task
    # Display all records
    # Search record
    # Edit record
    # Delete record

# Try to work with following databases
    # SQLLite - Free
    # MySQL - Paid
    # MariaDB - Free

    # MangoDB - Paid
    # DynamoDB - Paid
    # SQL Server - Paid
    # Oracle - Paid