'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

print("-------------------------------------------")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

print("-------------------------------------------")
'''
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
'''

print("--------------------USET INPUT-----------------------")
'''
userName = input("Enter a user name : ")
userId = input("Enter a user Id : ")
age = input("Enter your age : ")
print("User name is : ",userName)
print("User name is : ",userId)
print("User name is : ",age)

'''

print("--------------------String formating-----------------------")

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
myorder2 = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
print(myorder2.format(quantity, itemno, price))

age = input("Enter your age ")
name = input("Enter your name ")
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))