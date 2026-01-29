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

#day 2 code
class Person:
    def __init__(self,name):
        self.name = name 

class Job:
    def __init__(self,salary):
        self.salary = salary

class Employee(Person,Job):
    def __init__(self, name, salary):
        Person.__init__(self.name)
        Job.__init__(self.salary)

    def detais(self):
        print("Name",self.name)
        print("Salary",self.salary)
      

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):
    def department(self, dept):
        print(self.name, "manages", dept, "department")


# Object creation (outside the class)
# emp = Manager("Joy")

# emp.show_role()
# emp.department("HR")

# import numpy_q as np

# arr = np.linspace(0, 10, 5)
# print(arr)


# import numpy_q as np

# a =np.add(5,3)
# print(a)

# import numpy_q as np

# arr = np.array([10, 20, 30, 40, 50])

# print(np.mean(arr))



# a = np.array([[1,2],[3,4]])
# print(a.reshape(4))


# import numpy_q as np

# a =np.array([4,3,2,])
# a2 =np.sort(a)
# print(a2)

# class Dog:
#     # Class variable
#     species = "Canine"

#     def __init__(self, name, age):
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

class Person:
    def __init__(self, name):
        self.name = name


class Job:
    def __init__(self, salary):
        self.salary = salary


class Employee(Person, Job):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print("Name:", self.name)
        print("Salary is:", self.salary)


# Creating object
emp = Employee("akshay", 50000)

# Calling method
emp.details()


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):
    def department(self, dept):
        self.dept = dept

        print(self.name, "manages", self.dept, "department")

mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")


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


