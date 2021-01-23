# MySQL Library
# python -m pip install --upgrade pip
# pip install mysql-connector-python==8.0.11
import mysql.connector


def fileToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def binaryDataToFile(filename, binary_data):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(binary_data)


def insertBLOB(data):
    try:
        connection = mysql.connector.connect(host='localhost', database='db_corepython', user='root', password='')
        cursor = connection.cursor()
        sql_query = """ INSERT INTO tbl_person_photos(photo) VALUES (%s)"""
        # Convert data into tuple format
        values = (data, )
        result = cursor.execute(sql_query, values)
        connection.commit()
        print("Insert photo sucessfully", result)
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def updateBLOB(id, data):
    try:
        connection = mysql.connector.connect(host='localhost', database='db_corepython', user='root', password='')
        cursor = connection.cursor()
        sql_query = """ UPDATE tbl_person_photos SET photo=%s WHERE id=%s"""
        # Convert data into tuple format
        values = (data, id)
        result = cursor.execute(sql_query, values)
        connection.commit()
        print("Update photo sucessfully", result)
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def selectBLOB(id):
    try:
        connection = mysql.connector.connect(host='localhost', database='db_corepython', user='root', password='')
        cursor = connection.cursor()
        sql_query = """SELECT * from tbl_person_photos where id = %s"""
        values = (id,)
        cursor.execute(sql_query, values)
        record = cursor.fetchall()
        for row in record:
            id = row[0]
            tmp_file_name ="image_"+str(id)+".png"
            tmp_binary_data =row[1]
            binaryDataToFile(tmp_file_name, tmp_binary_data)
            print("Data Write on {}".format(tmp_file_name))
    except mysql.connector.Error as error:
        print("Error {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

# Insert Data
#binary_data = fileToBinaryData("image1.png")
#insertBLOB(binary_data)

# Update Data
binary_data = fileToBinaryData("image01.png")
print(binary_data)
updateBLOB(1, binary_data)

# Select Data
selectBLOB(1)