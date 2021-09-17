#Python Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)
f = ["apple", "banana", "cherry","apple"]
print(type(f))
fruts = set(f)
print(fruts)
print(type(fruts))

for x in thisset:
  print(x)
i=0

while i< len(thisset):
    print("This is while LOOP")
    i= i+1


thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print("This is adding list to set : ",thisset)

thisset.remove("mango")
print(thisset)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)