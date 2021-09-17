#Python Tuples
tuplename = ("apple","banana","mango")
print(tuplename)
print(tuplename[0])
if "apple" in tuplename:
    print("apple is in the tuple")

# can convert the tuple into a list, change the list, and convert the list back into a tuple
x = ("apple","banana","mango")
y = list(x)
y[1] = "pinapple"
y.append( "Lichi")
print(type(y))
x = tuple(y)
print(x)
print(type(x))

print(tuplename + x)

#unpacking a Tuple
print("------------unpacking a Tuple----------------")
fruits = ("apple","banana","mango")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

print("------------For Loop a Tuple----------------")

for x in range(len(fruits)):
    print(fruits[x])

print("------------While Loop a Tuple----------------")

i=0
while i < len(fruits):
    print(fruits[i])
    i = i + 2

c = fruits*2
print(c)
print("There are", c.count("apple"),"apple in c tuple")