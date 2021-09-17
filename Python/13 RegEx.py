#Python RegEx
import re
pattern = r"Cookie" #This r  is called a raw string literal
sequence = "Cookie"
if re.match(pattern,sequence):
    print("Match")
else:
    print("Not Match")



txt = "The rain in Spain"
x = re.search("rain",txt)
y = re.search("^The",txt)
if x:
    print("Yes")
if y:
    print("Found")
else:
    print("No")