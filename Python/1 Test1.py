

print("Hello, World!")
if 5 > 1:
    print("My name is Nahid")
    if 5 < 6:
        print("6 is larger")
print("------------------------------------")
#single line comment
"""
Multiple  line comment
using three cotation
"""
#variable
x=5
y="Hi"
name= 'NAHID'
print(y)
print(x)
print(type(x))
print(type(y))
print(name)
print("------------------------------------")
print("#####################################")



#multiple variable
a,b,c = 10,20,30
print(a)

#Global variable
name= 'NAHID Global' #This is global variable

def myfunction():
    name = "S M Nahid Local " # Same name as glabal variable but it is local
    global greeting
    greeting = "Hello "
    greetings= "Hi "
    print(greetings + name)
myfunction()

print(name)
print(greeting + name)
print("------------------------------------")




#binaru data type memoryview
binary = memoryview(bytes(5))
print(binary)
print(type(binary))
print("------------------------------------")
print("#####################################")




#Example of tuples inside list
info = [('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]
print(type(info))
print(info[1])

print("------------------------------------")
print("#####################################")




# Python Numbers
z = 1j
print(type(z))
zz = float(x)
print(zz)

import random
print(random.randrange(1,5))

print("------------------------------------")
print("#####################################")



#Python String

for n in "banana":
    print(n)
print(len(n))

txt = " This is a test to chacks if a char is present in a string"
print("test" in txt)
if "test" in txt:
    print("Yes, 'test' is present  ")

print("------------------------------------")
print("#####################################")
#Slicing string
print(txt[5:7])
print(txt[:7])
print(txt[10:])
print(txt[-20:-12])

print("------------------------------------")
#Modify String

print(txt.upper())
print(txt.lower())
print(txt.strip()) # strips methods removes any whitespace from begining
print(txt.replace("t", "f"))
print(txt.split("is"))
p = print(txt.split("is"))
print(type(p))

print("------------------------------------")
#String formating
name = "Nahid"
age = 23
text = "My name is "+ name + ". I am {}"
print(text.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt2 = "We are the so-called \"Vikings\" from the north."
print(txt2)
txt3 = "We are the so-called \n\"Vikings\" from the north."   #\n for new line
print(txt3)
print("------------------------------------")
print("#####################################")


#Python Booleans
num1 = 1
num2 = 3
num3 = 4

if num1 > num2:
    print("Value " +format(num1)+ " is greater than " + format(num2))
if num1 > num3:
    print("Value " +format(num1)+ " is greater than " + format(num3))
if num2 > num1:
    print("Value " +format(num2)+ " is greater than " + format(num1))
if num2 > num3:
    print("Value " +format(num2)+ " is greater than " + format(num3))
if num3 > num1:
    print("Value " +format(num3)+ " is greater than " + format(num1))
if num3 > num2:
    print("Value " +format(num3)+ " is greater than " + format(num2))


def boolTeste():
    return True
if boolTeste():
    print("Yes")
else:
    print("No")

print("------------------------------------")
print("#####################################")



#Python Operatirs
























