# Hello Python
from ast import While
import math
print("Hello, Python")
print('o----')
print(' ||||')

# String Multiple
print('*' * 10)

#Variable & Datatype
price = 10  # integer
price = 12.3  # float
name = 'Roky'  # string
is_busy = True  # boolen

price = 20
print(price)
price = 10.3
print(price)

# Input form user
name = input("Enter Your name : ")
print('Hello, ' + name + ' !!')

# Datatype conversion
birth_Year = input("Enter Your Birth Year :")
print(type(birth_Year))

age = 2022 - int(birth_Year)  # Type conversion Str to int
print(type(age))
print('You are now ' + str(age))  # Type conversion  int to str


# Strings
jobTitle = 'I am  a "System Engineer"'
print(jobTitle)
print(jobTitle[3:])  # printing by index position Sqer b []
print(jobTitle[-1])  # printing by index position
new = jobTitle[:]
print(new)

# Muliline string
aboutMe = '''
    I am  a "System Engineer". 
    I live in Bangladesh.
    i am now 26.
    '''
print(aboutMe)

# Formating String
fName = 'Rejaul'
lName = 'Islam'
fullName = fName + ' [' + lName + '] is a programmer'
print(fullName)

# Formating String
fullName = f'{fName} [{lName}] is  a Programmer'
print(fullName)

# String Method
print("lenth of your string " + str(len(fullName)))
print(fullName.upper())
print(fullName.lower())
print(fullName.find('i'))
print(fullName.replace('e', 'r'))

print(10**2)

# Math Function
x = 2.5
print(round(x))
print(abs(-32.3))

# Math Module
math.ceil(34.3)


# IF / ELSE
if (fName == 'Rejaul'):
    print("Rejaul")
else:
    print("Roky")

# Logical Oparetor (and/or)
if ((fName == 'Rejaul') and (lName == 'Islam')):
    print("Rejaul Islam")
else:
    print("Roky")

# Comparsion Oparetor (>,<,==, !=)

if (2 < 3):
    print('2<3')


# Loops

# While
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Loop done")

# For
for x in 'roky':
    print(x)
print('\n')

# Nested Loops
for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')
    print('\n')


# function
def fName(x):
    print("Value is :", int(x))


fName(40)


# Lambda function (small anonymous function)
def x(a): return a + 10


print(x(29))


def fulName(fName, lName): return fName + lName


print(fulName('Rejaul', ' Islam'))


# Arrary
cars = ["Ford", "Volvo", "BMW"]
print(cars)
print(cars[2])


# Class
class Car:
    brand = 'volvo'
    price = 1000


oc = Car
print(oc.brand)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)


p1 = Person('roky', 26)

print(p1.name)
print(p1.age)
