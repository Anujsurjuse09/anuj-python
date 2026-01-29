

name="Anuj"
print(name)
age = 20
print("my age is :",age)
age=25
s2=str(age)
print(s2)

n = 42
f = 4.2
s = "hello world"
li ={'key':'value'}
bool = True

print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(bool))

a,b = 5,10
a,b = b,a
print(a,b)

word = "python" 
length =len(word)
print("length of the word",length)

# a = 15
# b = 4
# print(a//b)
# print(a%b)
# print(a**b)
# print(a/b)

# a = 13
# b = 33
# print(a> b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a>= b)
# print(a <=b)

# a= True
# b = False

# print( a and b)
# print(a or b)
# print(not a)



a = 10     #note
b = 4
print(a&b)
print(a|b)
print(~a)
print(a^b)
print(a>>b)
print(a<<b)



a = 10 
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<=a
print(b)


a = 10
b = 20
c = a

print(a is not b)
print(a is c)

#x = 24
#y = 20
#list = (10,20,30,40,50)
#if (x not in list):
#| print("x is NOT present in given list")
##else:
#| print("x is present in given list")
#if (y in list)
#| print(" y is present in given list")
#else:
#| print("y is NOT present in given list")

print(100/ 10 *10)
print(5-2+3)
print(5-(2+3))
print(2 **3**2)

age = 20
if age >= 18:
    print("eligible to vote")

marks=45
res= " pass" if marks >= 40 else "fail"
print("result:",res)

li = ["greeks","for","greeeks"]  #
for index in range (len(li)):
    print([index])

# cnt = 20
# while (cnt<5):
#        cnt =cnt+1
#        print("hello jumbo")

for i in range (1,5):
     for j in range(i):
        print(i)
        print()

for letter in 'jumbosforjumbos':
     if letter == 'e' or letter == 's':
          break
     
          print('current letter:',letter)

for letter in 'jumbosforjumbos':
     pass
print('Last Letter :', letter)



# Basic Calculator Program

# print("Simple Calculator")
# print("Select operation:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number:"))

# if choice == '1':
#     print("Result:", num1 + num2)

# elif choice == '2':
#     print("Result:", num1 - num2)

# elif choice == '3':
#     print("Result:", num1 * num2)

# elif choice == '4':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")

# else:
#     print("Invalid Input")


s = "jumbosforjumbos"
print(s[0]) #first character
print([5])  #6th character


a = []
a.append(10)
print("After append(10):",a)
a.insert(0,5)
print("After insert(0,5):",a)
a.extend([15,20,25])
print("After extend([15,20,25]):",a)
a.clear()
print("After clear():",a)


a7 = 5
if a7 == 5 :
     print("ok")

