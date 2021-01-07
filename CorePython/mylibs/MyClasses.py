# __str__ method to print multiple variables

class Class6():
    # initializer method (function) with parameter
    def __init__(self, var1=0, var2=0):
        # instance variables
        self.var1 = var1
        self.var2 = var2
        self.var3 = 0

    # Getters function
    def getVar1(self):
        return self.var1

    def getVar2(self):
        return self.var2

    def getVar3(self):
        return self.var3

    # Setters function
    def setVar1(self, var1):
        self.var1 = var1

    def setVar2(self, var2):
        self.var2 = var2

    def setVar3(self, var3):
        self.var3 = var3

    # Process Function
    def calc_sum(self):
        self.var3 = self.var1 + self.var2

    def calc_dif(self):
        self.var3 = self.var1 - self.var2

    def calc_prd(self):
        self.var3 = self.var1 * self.var2

    def calc_div(self):
        self.var3 = round(self.var1 / self.var2, 2)

    def __str__(self):
        return (str(self.var1) + "," + str(self.var2) + "," + str(self.var3))

# Inheritance


class Class7():
    def __init__(self, var1=0, var2=0):
        self.var1 = var1;
        self.var2 = var2;

    # Getters
    def getVar1(self):
        return self.var1

    def getVar2(self):
        return self.var2

    # Setters
    def setVar1(self, var1):
        self.var1=var1

    def setVar2(self, var2):
        self.var2=var2

    def __str__(self):
        return str(self.var1)+", "+str(self.var2)


class Class8(Class7):# Inheritance Class8 - Sub Class and Class7 - Super Class
    def __init__(self, var1=0, var2=0, var3=0):
        super().__init__(var1, var2)
        self.var3 = var3

    # Getters
    def getVar3(self):
        return self.var3

    # Setters
    def setVar3(self, var3):
        self.var3 = var3

    # Process Functions
    def calc_sum(self):
        self.var3 = self.var1+self.var2

    def calc_dif(self):
        self.var3 = self.var1-self.var2

    def calc_prd(self):
        self.var3 = self.var1*self.var2

    def calc_div(self):
        self.var3 = round(self.var1/self.var2, 2)

    def __str__(self):
        return super().__str__()+", "+str(self.var3)

class Class9():
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    # Getters
    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def setNum1(self, num1=0):
        self.num1=num1

    def setNum2(self, num2=0):
        self.num2=num2

    def __str__(self):
        return str(self.num1)+", "+str(self.num2)

    # Operator Overloading
    # + Add Operator
    def __add__(self, other):
        return self.num1 + other.num1, self.num2 + other.num2

