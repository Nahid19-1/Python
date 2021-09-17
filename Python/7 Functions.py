#Python Functions

def my_Function(fname):
    print("Name : " + fname)

my_Function("Nahid")
my_Function("Anik")

def name(fname,lname):
    print("First Name : "+fname +"\n" +"Last Name : "+lname)
name("S. M.","Nahid")

#for unknown argument
print("------------------#for unknown argument#-------------------")
def student(*info):
    print("First Student Name is : "+ info[2])
student("Sakib","Nahid","Anik")

print("------------------#Default Parameter Value#-------------------")
def my_country(country="Bangladrsh"):
    print("I an from : " + country)

my_country("Japan")
my_country("India")
my_country()
my_country("USA")


c=["India","Japan","USA"]
my_country(str(c))

#Passing a List as an Argument
def my_fruits(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_fruits(fruits)

print("------------------#Return value#-------------------")
def multi(x):
    result = 5*x
    return result
print("The result of 5*x is :",multi(2))
print(multi(3))
print(multi(5))

print("------------------#Recursion#-------------------")
def recursion(k):
    if (k > 0):
        result = k +recursion(k-1)
        print(result)
    else:
        result=0
    return result

print("\n\nRecursion Example Results")
recursion(6)
'''
tri_recursion(6) = 6 + tri_recursion(5)
So to get the result for tri_recursion(6) we must get the result of tri_recursion(5) 
Following this logic, the problem reduces to:

tri_recursion(6) 
 = 6 + tri_recursion(5) 
 = 6 + 5 + tri_recursion(4)
 = 6 + 5 + 4 + tri_recursion(3)
 = 6 + 5 + 4 + 3 + tri_recursion(2)
 = 6 + 5 + 4 + 3 + 2 + tri_recursion(1)
 = 6 + 5 + 4 + 3 + 2 + 1 + tri_recursion(0)
 
 tri_recursion(6)= 6 + 5 + 4 + 3 + 2 + 1 = 21
 tri_recursion(5)= 5 + 4 + 3 + 2 + 1 = 15
 tri_recursion(4)= 4 + 3 + 2 + 1 = 10
 tri_recursion(3)= 3 + 2 + 1 = 6
 tri_recursion(2)= 2 + 1 = 3
 tri_recursion(1)= 1 = 1
 
'''