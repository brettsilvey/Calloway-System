import os

def apply_function(func, x):
   return func(x)

def square(x):
   return x ** 2

print(square(3))

result = apply_function(square, 3)
print(result)