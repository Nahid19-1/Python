#Python JSON
import json
print("---------------Jaon to Python------------")
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print("This is Json type  :",type(x))


# parse x: The result will be a Python dictionary.
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print("After convert  Json to python  type  :",type(y))




print("---------------------Python to Json----------------------")
x= {
    "Name : " : "Nahid",
    "Id : " : "19-39998-1",
    "Age : ": 23
}
print("This is Python type  :",type(x))
#convert into json
y = json.dumps(x)
print(y)
print("After convert Python to Json  type  :",type(y))