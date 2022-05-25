# Hello Python
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
if ((fName == 'Rejaul') and (lName =='Islam')):
    print("Rejaul Islam")
else:
    print("Roky")
 
# Comparsion Oparetor (>,<,==, !=)

if (2<3):
    print('2<3')


