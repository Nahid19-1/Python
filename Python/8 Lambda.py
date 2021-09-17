#Python Lambda
x = lambda a,b,c: a + b + c
print(x(2,2,2))

def my_function(n):
    return lambda a: a*n

double = my_function(2)
triple = my_function(3)
print(double(22))
print(triple(22))