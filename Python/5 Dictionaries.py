#Python Dictionary
student1 = {
    "name":"Nahid",
    "Id":"19-39998-1",
    "CGPA":3.8
}
print("Full info : ",student1)
print("Student name is : ",student1["name"])
sid = student1.get("Id")
print("Student Id is : ",sid)
skey = student1.keys()
print("Return only the keys : ",skey)

svalue = student1.values()
print("Return only the values : ",svalue)

student1["semister"] = "8th"
print("Updated Full info : ",student1)

sitem = student1.items()
print("Return Dictionaty as a tuple in list : ",sitem)

if "name" in student1:
    print("Yes name is exist")

student1["semister"] = "7th"
print(student1)

student1.update({"age":23})
print("Adding age using update : ",student1)

student1.pop("semister")
print("Semister poped : ",student1)

print("----------FOR LOOP-----------")
print("----------Only value print-----------")

for x in student1.values():
    print(x)
print("----------Only Key print-----------")
for x in student1.keys():
    print(x)
print("----------Both value & key print-----------")
for x,y in student1.items():
    print(x ,":",y)
print("#############-----NESTED Dictionary-----#############")

student2 = {
    "name":"Anik",
    "Id":"19-46365-1",
    "CGPA":3.7,
    "age":23
}
student3 = {
    "name":"Sakib",
    "Id":"19-40018-1",
    "CGPA":3.9,
    "age":23
}

student = {
    "Student1":student1,
    "Student2":student2,
    "Student3":student3
}

print("All student info :",student)

for x,y in student.items():
    print(x," : ",y)

