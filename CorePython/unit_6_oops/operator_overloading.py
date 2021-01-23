class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a

obj1 = A(10)
obj2 = A(30)
obj3 = obj1 + obj2
print(obj3)

print(dir(A))
print(help(A))