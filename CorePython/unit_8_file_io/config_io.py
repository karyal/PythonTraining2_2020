# pip install configparser
import configparser
import sys

FILE_NAME = "config.ini"

def write_config():
    try:
        parser = configparser.ConfigParser()
        parser.add_section("USER")
        parser.set("USER","USER_NAME","ADMIN")
        parser.set("USER","USER_PASS","78901")
        file = open(FILE_NAME, "w")
        parser.write(file)
        file.close()
    except:
        print("Error : "+sys.exc_info()[0])

def read_config():
    try:
        parser = configparser.ConfigParser()
        parser.read(FILE_NAME)
        for section in parser.sections():
            print("["+ section+"]")
            for key, value in parser.items(section):
                print("{} = {}".format(key, value))
        print()
    except:
        print("Error : "+sys.exc_info()[0])

#write_config()
read_config()