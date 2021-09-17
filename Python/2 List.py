#Python Lists

foodList = ["apple", "mango", "banana", "orange"]
print(foodList)
print(len(foodList))
if "banana" in foodList:
    print(type(foodList))
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.
"""
print(foodList[1:3])
foodList[1] = "melon"
print(foodList)

foodList.insert(4,"berry")
print(foodList)

foodList.append("Jackfruit")
print(foodList)

lap = ["Acer", "MSI"]
foodList.extend(lap)
print(foodList)

foodList.remove("Jackfruit")
print(foodList)

foodList.pop(3)
print(foodList)

#foodList.clear()
#print(foodList)
print('--------------LOOP LIST---------------')
print('--------------For LOOP ---------------')

for x in foodList:
    print(x)
print("___________________________")

for i in range(len(foodList)):
    print(foodList[i-1])

print('--------------While LOOP ---------------')
i=0
while i < len(foodList):
    print(foodList[i])
    i= i+1

#Short foor loop
print('--------------Short FOR LOOP ---------------')
[print(a) for a in foodList]

student = ["Nahid","Sakib", "Anik","Kajol"]
name =[]
for x in student:
    if "i" in x:
        name.append(x)
print(name)

print("-----------------------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist =[x.upper() for x in fruits]
print(newlist)

newlist = ["Fuck You" for x in fruits]
print(newlist)

print('--------------Sort List ---------------')
food = ["orange", "mango", "apple", "pineapple", "banana"]
food2 = ["Orange", "Mango", "apple", "pineapple", "banana"]
food.sort()
print(food)

food.sort(reverse=True)
print(food)

print(food2)
food2.sort(key = str.lower)
print(food2)

print('--------------Copy List ---------------')
food3 = food.copy()
print(food3)

food5 = food2 + food3
print(food5)

food5.extend(food)
print(food5)