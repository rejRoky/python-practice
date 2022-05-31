from unittest import result


print("-----------------------")
print("------Calculator-------")
print("-----------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("-----------------------")

k = int(input("Enter option 1 to 4 , What you want: "))
print("-----------------------")

print("Enter Two Number one bye one : ")
a = input("1st Number: ")
b = input("2nd Number: ")
print("-----------------------")

def add ():
    print ("Result: ", a+b)

def sub ():
    print ("Result: ", a-b)

def mul ():
    print ("Result: ", a*b)

def div ():
    print ("Result: ", a/b)

if (k == 1):
    add()

elif (k == 2):
    sub()

elif (k == 3):
    mul()

elif (k == 4):
    div()
