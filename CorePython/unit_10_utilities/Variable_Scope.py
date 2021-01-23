var1 ="Kathmandu, Nepal" # Global (Module Level)
def outer():
    var2 = "Lalitpur, Nepal" # Global Function Level (i.e Local Variable)
    def inner():
        var3 ="Bhaktapur, Nepal" # Global Funcation Level (i.e Local Variable)
        print(var1, var2, var3)
    inner()

outer()

def outer1():
    var4 = "Lalitpur, Nepal" # Global Function Level
    def inner1():
        nonlocal var4
        var4 = "Bhaktapur, Nepal"  # Global Funcation Level
        print(var4, var4)
    inner1()

outer1()