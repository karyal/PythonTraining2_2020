import pickle
import sys

# Write on file
example_dict = {1:"6",2:"2",3:"f"}
pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

# Reading from file
pickle_in = open("dict.pickle","rb")
obj2 = pickle.load(pickle_in)
print(obj2)

class Person():
    def __init__(self, id, name):
        self.id=id
        self.name=name
    def __str__(self):
        return str(self.id)+", "+self.name

# Write Object on File
try:
    obj1 = Person(1,"Raj Tahapa")
    file1 = open("data2.obj", 'wb')
    pickle.dump(obj1, file1)
    file1.close()
except:
    print("Error : "+str(sys.exc_info()[1]))

# Append Object on File
try:
    obj2 = Person(2,"Kiran Rana")
    file1 = open("data2.obj", 'ab')
    pickle.dump(obj2, file1)
    file1.close()
except:
    print("Error : "+str(sys.exc_info()[1]))


# Reading Object from File
try:
    file2 = open('data2.obj', 'rb')
    obj=pickle.load(file2)
    file2.close()
except:
    print("Error : " + str(sys.exc_info()[1]))


class Person():
    def __init__(self, id, name):
        self.id=id
        self.name=name
    def __str__(self):
        return str(self.id)+", "+self.name

# Writting Ovjects-1
with open('data.pkl', 'wb') as f:
    obj1 = Person(1, "Raj Tahapa")
    obj2 = Person(2, "Kiran Rana")
    pickle.dump(obj1 , f)
    pickle.dump(obj2, f)

# Reading Ovjects-1
with open('data.pkl', 'rb') as f:
    obj = pickle.load(f)
    print(obj)
    obj = pickle.load(f)
    print(obj)

# Reading Objects-2
with open('data.pkl', 'rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            print(obj)
        except:
            break