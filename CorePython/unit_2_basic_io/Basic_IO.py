#Input
var1 = input("Enter any number : ")

# Output
print(var1)
print("Label : ", var1)
print("Label : {}".format(var1))
print(f"Label : {var1}", )
print("Label : %s"%var1)

# Write on file
f = open("info.txt","w+")
f.write("Hello")
f.close()

# Reading from file
f = open("info.txt","r")
str = f.read()
print(str)
f.close()

# Note
# We can save in database and retrieve from database too
# References.txt: Unit-9 [DBMS]