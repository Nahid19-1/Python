#Python if/else
a =11
b =5
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than b")


#Short from of if
if a>b: print("A is greater than B")

x=10
y=20
print("X") if x>y else print("Y")

f1=30
f2=30
print("F1") if f1>f2 else print("F1=F2") if f1==f2 else print("F2")

c =12
if a>b and c>b:
    print("Both condition are true")

if a>b or a>c:
    print("Only one condition are true")
print("-------------------------------------------")
print("-------------------Nested if------------------------")
if a>10:
    print("Greater than 10")
    if a>20:
        print("Greater than 20")
    else: print("But Not Greater than 20")


print("-------------------While Loop------------------------")

#While Loop
i=0
while i<6:
    print(i)
    i= i+1
    if i==4:
        print("Value of i is 4")
        break

print("-------------------For Loop------------------------")

#For Loop
for x in "Nahid":
    print(x)
    if x=="h":
        break

print("-------------------Range------------------------")
for x in range(2,10,3):
    print(x)

print("-------------------Nested for------------------------")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print("Adj value :  ",x ,"  Fruits value :  " ,y)
