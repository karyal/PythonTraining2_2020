import sys
import mysql.connector
from libs.functions import read_db_config

def connect1():
    # Connect MySQL Database Server
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password =''
        )
        conn.close()
        print("Connect database server sucessfully")
    except:
        print("Error : "+ sys.exc_info()[1])

def connect2():
    # Connect MySQL Database Server with MySQL Database
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password ='',
            database = 'db_corepython'
        )
        if conn.is_connected():
            print("Connect database successfully")
            conn.close()
    except:
        print("Error : "+ sys.exc_info()[1])


def connect3():
    # Connect MySQL Database Server with MySQL Database
    db_info = {'host':'localhost','database':'db_corepython','user':'root','password':''}
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            print("Connect database successfully")
            conn.close()
    except:
        print("Error : "+ sys.exc_info()[1])


def connect4():
    # Connect MySQL Database Server with MySQL Database
    db_info = read_db_config()
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            print("Connect database successfully")
            conn.close()
    except:
        print("Error : "+ sys.exc_info()[1])

# Insert Record
# Table
"""
    CREATE TABLE `tbl_person` (
      `id` int(11) NOT NULL,
      `full_name` varchar(50) NOT NULL,
      `contact_address` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""

def insert_record1():
    db_info = {'host':'localhost','database':'db_corepython','user':'root','password':''}
    sql_query ="""
                insert into tbl_person(full_name, contact_address) values('Krishna','KTM')
               """
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query)
            conn.commit()
            print("Insert record on table successfully")
    except:
        print("Error : "+ sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def insert_record2():
    db_info = {'host':'localhost','database':'db_corepython','user':'root','password':''}
    sql_query ="""insert into tbl_person(full_name, contact_address) values(%s, %s)"""
    values = ('Rajan Rai','Lalitpur')
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query, values)
            conn.commit()
            print("Insert record on table successfully")
    except:
        print("Error : "+ sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def insert_record3():
    db_info = {'host':'localhost','database':'db_corepython','user':'root','password':''}
    sql_query ="""insert into tbl_person(full_name, contact_address) values(%s, %s)"""
    values = [
        ('Kiran Rimal','Bhaktapur'),
        ('Reeta Shrestha', 'Lalitpur'),
        ('Kedar Rijal', 'KTM'),
    ]
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.executemany(sql_query, values)
            conn.commit()
            print("Insert record on table successfully")
    except:
        print("Error : "+ sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def select_record1():
    # Connect MySQL Database Server with MySQL Database
    db_info = read_db_config()
    sql_query = """SELECT * FROM tbl_person"""
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query)
            row = cursor.fetchone()
            while row is not None:
                print(row)
                row = cursor.fetchone()
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def select_record2():
    # Connect MySQL Database Server with MySQL Database
    db_info = read_db_config()
    sql_query = """SELECT * FROM tbl_person"""
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            print("Total rows : ", cursor.rowcount)

            for row in rows:
                print(row)
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()


def update_record1():
    # Connect MySQL Database Server with MySQL Database
    db_info = read_db_config()
    sql_query = """UPDATE tbl_person SET full_name='New Name', contact_address='New Address' where id=1"""
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query)
            conn.commit()
            print("Update record successfully")
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def update_record2():
    # Connect MySQL Database Server with MySQL Database
    db_info = read_db_config()
    sql_query = """UPDATE tbl_person SET full_name=%s, contact_address=%s where id=%s"""
    values = ('New Name','New Address',1)
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query, values)
            conn.commit()
            print("Update record successfully")
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def delete_record1():
    # Connect MySQL Database Server with MySQL Database
    db_info = read_db_config()
    sql_query = """DELETE from tbl_person where id=5"""
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query)
            conn.commit()
            print("Delete record successfully")
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

def delete_record2():
    # Connect MySQL Database Server with MySQL Database
    db_info = read_db_config()
    sql_query = """DELETE from tbl_person where id=%s"""
    values = (4, )
    try:
        conn = mysql.connector.connect(**db_info)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql_query, values)
            conn.commit()
            print("Delete record successfully")
    except:
        print("Error : " + sys.exc_info()[1])
    finally:
        cursor.close()
        conn.close()

#connect1()
#connect2()
#connect3()
#connect4()
#insert_record1()
#insert_record2()
#insert_record3()
#select_record1()
#select_record2()
#update_record1()
#update_record2()
#delete_record1()
#delete_record2()

# References.txt
#https://pynative.com/python-mysql-database-connection/