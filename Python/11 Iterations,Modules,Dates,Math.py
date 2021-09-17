#Python Iterators
print("---------------------Python Iterators----------------------")
fruits = ["Mango","Orange","Banana","Barry"]
myit = iter(fruits)
print(myit)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

my_String ="nahid"
for x in my_String:
    print(x)

class my_Numbers:
    def __iter__(self):
        self.first = 1
        return self

    def __next__(self):
        if self.first<=5:
            new = self.first
            self.first = 1+new
            return new
        else:
            raise StopIteration


myclass = my_Numbers()
myiter = iter(myclass)

for x in myiter:
    print(x)







#Python Scope
print("---------------------Python Scope----------------------")
a = 10
def my_funnction():
    xx = 5
    def printfunction():
        print("Local only inside the scop : ",xx)
        print("Global function : ",a)
    printfunction()

my_funnction()
#print(xx)#local function can't ust outside the scop
print(a)






#Python Modules
print("---------------------Python Modules----------------------")
import module
s1 = module.Student("Nahid",12)
s2 = module.Student("Sakib",13)

'''
import module as sinfo
s1 = sinfo.Student("Nahid",12)
'''

print("----------------------------------------")
import platform
x = platform.processor()
y = platform.release()
s = platform.system()
v = platform.version()
print("This is info about processor :  ",x)
print("This is info about release :  ",y)
print("This is info about system :  ",s)
print("This is info about version :  ",v)


print("----------------------------------------")

from module import person1
print (person1)


#Python Dates
print("-------------------Python Dates---------------------")

import datetime

dt  = datetime.datetime.now()
print("year, month, day, hour, minute, second, and microsecond.")
print(dt)
print("Year : ",dt.year)
print("Month : ",dt.month)
print("Day : ",dt.day)
print("Hour : ",dt.hour)
print("Minute : ",dt.minute)

date = dt.strftime("%m/%d/%Y ")
time = dt.strftime("%H/%M/%S")
print("Date :",date +"\n" +"Time :",time)


#Python Math
print("-------------------Python Math---------------------")
import math
x = min(4,5,6)
y = max(4,5,6)
print(x)
print(y)

x = math.sqrt(64)
print(x)

x = math.pi
print(x)