from libs.MyClasses import *

# Animal Class
animal = Animal()
print(type(animal))
print(id(animal))
#print(len(animal)) # TypeError: object of type 'Animal' has no len()
print(animal)

# Person Class
person1 = Person()
print(type(person1))
print(id(person1))

print(person1.id,", ", person1.name)
print(person1)

person2 = person1
print(id(person1))
print(id(person2))

person2.id=person1.id
person2.name=person1.name
print(id(person1))
print(id(person2))

# Student Class
student1 = Student()
student1.setId(2)
student1.setName("Kiran Rana")
student1.setGrade("BBA")
student1.setSection("A")

print(type(student1))
print(id(student1))
print(student1.toString())
print(student1)

# Constructor
student3 = NewStudent()
student4 = NewStudent(1, "Rajan Nepal")
print(student3)
#print(student4)

person3 = C1(1, "Raj Rai")
print(person3)

tmp = C4(1, "Krishna")
tmp.setId(2)
tmp.setName("Krishna Aryal")
print(tmp)

tmp = C5(1,"Krishna","Kathmandu","krishna@gmail.com","9851121314")
print(tmp)