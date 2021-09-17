#Python Arrays
import array as arr
cars = arr.array("i",[2, 4, 6])
print(type(cars))

#Python Classes and Objects
print("-------------#Python Classes#---------")
class my_Class:
    a=5
m1 = my_Class
print(m1.a)

class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def desplay(self):
        print("Student name is : ", self.name)
        print("Student id is : ", self.id)

s1 = student("Nahid","19-39998-1")
s1.desplay()

class person:
    def __init__(person_info,name,age):
        person_info.name = name
        person_info.age = age

    def display_person(info):
        print("Name is : ",info.name)
        print("Age is : ",info.age)


p1 = person("Rahim","34")
p1.display_person()