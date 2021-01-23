import csv
import sys

FILE_NAME = "data1.csv"

def write_csv1():
    try:
        nums = [[1,2,3,4,5],[6,7,8,9,10]]
        file = open(FILE_NAME, "w")
        with file:
            writer = csv.writer(file)
            for row in nums:
                writer.writerow(row)
            print("Write on csv file")
        file.close()
    except:
        print("Error : "+sys.exc_info()[0])

def read_csv1():
    try:
        file = open(FILE_NAME, "r")
        with file:
            reader = csv.reader(file)
            for row in reader:
                if len(row)>=1:
                    print(row, end="\n")
        file.close()
    except:
        print("Error : "+sys.exc_info()[0])

FILE_NAME = "data2.csv"

def write_csv2():
    try:
        file = open(FILE_NAME, "w")
        with file:
            fields = ["first_name","last_name"]
            writer = csv.DictWriter(file, fields)
            writer.writeheader()
            writer.writerow({"first_name":"Raj","last_name":"Thapa"})
            writer.writerow({"first_name": "Kiran", "last_name": "Rai"})
        file.close()
    except:
        print("Error : "+sys.exc_info()[0])

def read_csv2():
    try:
        file = open(FILE_NAME, "r")
        with file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
        file.close()
    except:
        print("Error : "+sys.exc_info()[0])

#write_csv1()
#read_csv1()

#write_csv2()
read_csv2()