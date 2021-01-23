import sys

FILE_NAME = 'data1.txt'
FILE_NAME = 'C:\\Users\\info_\\Desktop\\Working\\Python\\CorePython01\\unit_8_file_io\\data1.txt'
FILE_NAME = 'C:/Users/info_/Desktop/Working/Python/CorePython01/unit_8_file_io/data1.txt'

def create_file():
    try:
        file = open(FILE_NAME, "w")
        print("File open successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()


def write_data1():
    try:
        file = open(FILE_NAME, "w")
        file.write("Hello world of File IO")
        print("Write content on file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()


def write_data2():
    try:
        file = open(FILE_NAME, "w")
        file.writelines("Hello world of File IO Line-1")
        file.writelines("Hello world of File IO Line-2")
        print("Write content on file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def write_data3():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.write("First Line\n")
            file.write("Second Line\n")
            file.write("Third Line\n")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def append_data():
    try:
        file = open(FILE_NAME, "a")
        file.write("Hello world of File IO Line 2")
        print("Append content on file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()


def read_data1():
    try:
        file = open(FILE_NAME, "r")
        #contents = file.read(5) # Hello
        contents = file.readline() # Hello world of File IO Line-1Hello world of File IO Line-2
        contents = file.readlines()
        for content in contents:
            print(content)
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def read_data2():
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            print(line)
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

#create_file()
#write_data1()
#write_data2()
#append_data()
#read_data1()
#write_data3()
#read_data2()