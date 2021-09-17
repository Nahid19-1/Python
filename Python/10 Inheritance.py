#Python Inheritance
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def print_Name(self):
        print("Full name : ",self.firstname,self.lastname)

p1= Person("S. M.","Nahid")
p1.print_Name()


class Student(Person):
    def __init__(self,sname,lname):
        super().__init__(sname,lname)
        self.gradution = 2023
s1= Student("Lokman", "Hossain")
s1.print_Name()
print("Graduation Year :",s1.gradution)


print("-------------This is for Studeny2 Class------------")
class Student2(Person):
    def __init__(self,sname,rname,year):
        super().__init__(sname,rname)
        self.gradution = year


    def welcome(self):
        print("Welcome ",self.firstname,self.lastname,"to the class of ",self.gradution,"semister")

s2= Student2("Skaib", "Al Hassan",2011)
s2.print_Name()
print("Graduation Year :",s2.gradution)


s3 = Student2("Tammim","Iqbal","9th")
s3.welcome()

