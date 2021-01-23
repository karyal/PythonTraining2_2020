class Animal():
    pass

class Person():
    def __init__(self):
        self.id = 1
        self.name="Raj Rai"

    def __str__(self):
        return(str(self.id)+", "+self.name)


class Student():
    def __init__(self):
        self.id = 1
        self.name = "Rajan Thapa"
        self.grade= "BIT"
        self.section= "A"

    def getId(self):
        return self.id

    def setId(self, id):
        self.id=id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getGrade(self):
        return self.grade

    def setGrade(self, grade):
        self.grade= grade

    def getSection(self):
        return self.section

    def setSection(self, section):
        self.section= section

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.grade+", "+self.section

    def toString(self):
        return str(self.id)+", "+self.name+", "+self.grade+", "+self.section

class NewStudent():
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name

    """
    def __init__(self):
        self.id = 0
        self.name = ""
    """

    def __str__(self):
        return str(self.id)+", "+self.name
class C1():
    id =0
    name=""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def __str__(self):
        return str(self.id)+", "+self.name


class C2():
    address=""
    email = ""

    def __init__(self, address, email):
        self.address = address
        self.email = email

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def setAddress(self, address):
        self.address = address

    def setEmail(self, email):
        self.email = email

    def __str__(self):
        return self.address+", "+self.email


class C3():
    mobile=""
    def __init__(self, mobile):
        self.mobile=mobile

    def getMobile(self):
        return self.mobile

    def setMobile(self, mobile):
        self.mobile=mobile

    def __str__(self):
        return self.mobile


class C4(C1):
    def __init__(self, id, name):
        C1.__init__(self, id, name)


class C5(C1, C2, C3):
    def __init__(self, id, name, address, email, mobile):
        C1.__init__(self, id, name)
        C2.__init__(self, address, email)
        C3.__init__(self, mobile)

    def __str__(self):
        return C1.__str__(self)+", "+C2.__str__(self)+", "+C3.__str__(self)