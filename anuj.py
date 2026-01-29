#string in python

s = "jumbosforjumbos"
print(s[0]) #first character
print([5])  #6th character

s = "jumbosfor"
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[-3:])
print(s[:-3])


s = "python" 
for var in s:
    print(var)

s = "jumbosforjumbos"
s = "G" + s[:-5]
print(s)

s = "jumbosforjumbos"
s = "G" + s[::-5]
# sequence[start : end : step]
print(s)


s = "hello jumbo"
s1 = "H"+ s[1:]
s2 = s.replace("jumbo","jumbosforjumbos")
print(s1)
print(s2)

s = "hello World"
print(s.upper())
print(s.lower())

s = "  Gfg  "               
print(s.strip())#remove extra spaces from a string

s = "python is fun "
print(s.replace("fun","_awesome"))


s1="hello"
s2="world"
print(s1 + " " + s2)


s1 = "Hii"
print(s1 * 3)


s = "jumbosforjumbos"
print("Jumbos" in s)
print("gfg" in s)


#List in python

a = [1,2,3,4,5] #list of integers
b = ['apple','banana','cherry']
c = [1, a , True]

print(a,b,c)


a =[2]*5
print(a)

a =["2"]*5
print(a)

a = [10,20,30,40,50]
a.insert(4,25)
print(a)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[0][0])

a = list((1, 2, 3, 'appple', 4.5))
print(a)
b = list("JFG")
print(b)


#tupple in python

tup = (s,'welcome',7,'Jumbo')
print(tup)

tup1 = (0,1,2,3)
tup2 = ('python','greek')
tup3 = (tup1,tup2)
print(tup3)

tup1 = ('jumbo',)*3
print(tup1)



tup1 = (0,1,2,3)
tup2 = ('python','greek')
tup3 = (tup1,tup2)
print(tup3)

tup1 = ('jumbo',)*3
print(tup1)

tup  = (1,2,3,4,5,6)
a,*b,c = tup
print(a)
print(b)
print(c)

#accessing tuple with indexing
tup = tuple("jumbo")
print(tup[0])
#accessing a range of elements using slicing
print(tup[1:4])
print(tup[:3])

#tuple unpacking
tup = ("jumbo","for","jumbo")
#this line unpack values of tuple
a,b,c, = tup
print(a)
print(b)
print(c)

tup = (5,'welcome',7,'jumbo')
print(tup)

#creating a tuple with nested tuple
tup1 = (0,1,2,3)
tup2 = ('python','greek')
tup3 = (tup1,tup2)
print(tup3)

#creating a tuple with repetition
tup1 = ('jumbo',)*3
print(tup1)

#creating a tuple with the use of loop
tup = ('jumbo',)
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

squares = [x**2 for x in range(1, 6)]
print(squares)


#data types
# 1.tuple
# 2.list
# 3.dictionary


# create dictionary using dict() constructor

d1 = {1:'jumbo',2: 'for',3:'jumbo'}
print(d1)

d2 = dict(a="jumbo",b= "for",c ="jumbo")
print(d2)


d = {1: 'geeks',2:'for',3:'greeks'}
d[4] ='geeks'
d[1] = "age : 22"
print(d)

d = {"name" : "anuj",1:"python",(1,2):[1,2,4]}
#acess using key
print(d[1])
#access using get
print(d.get("name"))


#Sets in python

set1 = set()
print(set1)
set1 = set("jumboforjumbo")
print(set1)
#creating a set with the use of list
set1= set(["jumbo","for","jumbo"])
print(set1)
#creating a set with the use of tuple
tup = ("jumbo","for","jumbo")
print(set(tup))
#creating a set with the use of dictionary
d = {"jumbo":1,"for":2,"jumbo":3}
print(set(d))


set1 = {3,1,4,1,5,9,2}
print(set1)#output may vary :{3,1,4,1,5,9,2}
#unindexed: acccessing elements by undex is not possible
#this will raise a typError
try:
    print(set1[0])
except TypeError as e:
    print(e)

#creating a 
set1 = {1,2,3}
#add one item
set1.add(4)

#add multiple item
set1.update([5,6])
print(set1)



set1 = set(["jumbo","for","jumbo."])
#acccesing element using loop
for i in set1:
      print(i,end="")
#checking the element using in keyword
print("jumbo" in set1)


set1 = {1,2,3,4,5,}
set1.remove(3)
print(set1)
try:
    set1.remove(10)
except KeyError as e:
    print("error:",e)

#attempting to discard an element that does not exist
set1.discard(4)# no error raised
print(set1)
set1.discard(10)
print(set1)


set1= {1,2,3,4,5}
val =set1.pop()
print(val)
print(set1)
#using pop on an empty set
set1.clear()#clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print("error:",e)

fset = frozenset([1,2,3,4,5])
print(fset)
set1= {3,1,4,1,5}
fset= frozenset(set1)
print(fset)

li = [1,2,3,3,4,5,5,6,2]
set1=set(li)
print(set1)

s="jumboforjumbo"
set1 = set(s)
print(set1)


d= {1:"one",2 :"two",3:"three"}
set1 =set(d)
print(set1)


a = [10,20,30,40,50]
a.remove(30)
print('after remove(30):',a)

popped_val = a.pop(1)
print("popped element:",popped_val)
print("after pop(1)",a)
del a[0]
print("after del a[0:]",a)



#class and attributes

class Dog:
    species = "canine"
    gender = "male"
    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = Dog("buddy",3) 
print(dog1.name)
print(Dog.species)
print(Dog.gender)


##self parameter

# class Dog:
#     # Class variable
#     species = "Canine"

#     def _init_(self, name, age):
#         # Instance variables
#         self.name = name
#         self.age = age

# #create objects
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# # Access class and instance variables
# print(dog1.species)   # (Class variable)
# print(dog1.name)      # (Instance variable)
# print(dog2.name)      # (Instance variable)

# # Modify instance variables
# dog1.name = "Max"
# print(dog1.name)      # (Updated instance variable)

# # Modify class variable
# Dog.species = "Feline"
# print(dog1.species)   # (Updated class variable)
# print(dog2.species)



#oops
#1.inheritance
#2.polymorphism--one name many forms
#3.encapsulaion
#4.Abstraction

class Animal:            # parent class
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):       # child class
    def sound(self):
        print(self.name, "barks")
# creating object
d = Dog("Buddy")
d.info()
d.sound()




class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

class GoldenDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name} guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GoldenDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


#single inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):     # Child class
    def show_role(self):
        print(self.name, "is an employee")
# Creating object
emp = Employee("Anuj")

# Accessing methods
print("Name:", emp.name)
emp.show_role()



#multiple inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job):   # Multiple Inheritance
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

# Creating object
emp = Employee("Anuj", 50000)

# Calling method
emp.details()


#multilevel inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):
    def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")



#polymorphism
# compile type polyorphism
class Calculator:
    def multiply(self,a=1,b=1,*args):
        result=a*b
        for num in args:
           result*=num
        return result
    
calc=Calculator()

print(calc.multiply())
print(calc.multiply(4))

print(calc.multiply(2,3))
print(calc.multiply(2,3,4))



#encapsulation
#public member
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Subemployee(Employee):
    def info(self):
        print("Age:", self.age)

# Creating object
emp = Subemployee("Ross", 30)

print("Name:", emp.name)
emp.info()



# encapsulation code(Getter & Setter with Validation)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private variable

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter with validation
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary! Salary must be positive.")

# Creating object
emp = Employee("Anuj", 50000)

# Getting salary
print("Salary:", emp.get_salary())

# Setting new salary
emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())

# Trying invalid salary
emp.set_salary(-2000)



#abstraction
from abc import ABC
# Abstract Base Class
class Dog(ABC):

    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def display_name(self):
        print("Dog name:", self.name)


# Child class
class Labrador(Dog):
    def sound(self):
        print(self.name, "says: Woof Woof!")


# Child class
class Beagle(Dog):
    def sound(self):
        print(self.name, "says: Bark Bark!")


# Creating objects
dogs = [
    Labrador("Buddy"),
    Beagle("Charlie")
]

# Loop through each dog
for dog in dogs:
    dog.display_name()
    dog.sound()
