# pip install SQLAlchemy
# pip install psycopg2

import psycopg2
import sys

#Connection parameters
param_dic = {
    "host"      : "john.db.elephantsql.com",
    "database"  : "jssslfkj",
    "user"      : "jssslfkj",
    "password"  : "IgMQ6d4QzLNJ0Y0hhH_wld_XnLW3ox-1"
}

def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**param_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    return conn

def single_insert(conn, values):
    """ Execute a single INSERT request """
    sql_query = """INSERT into flights(Flight_From, Flight_To, Airlines, Duration) values('%s', %s, %s, %s);"""
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query, values)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()
    #conn.close()

def main():
    conn = connect()
    values=('Kathmandu','Pokhara','Buddha Air', 30)
    single_insert(conn, values)