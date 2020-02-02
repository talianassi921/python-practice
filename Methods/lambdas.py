# function that has no name is a lambda
# can only be one line
# lambda parameter: single_expression
# expression is automaticlaly returned, so no return function
# when you pass in a function to another function
# it will not be used again

def square(num): return num **2

square2 = lambda num: num**2

add = lambda a,b: a+b

print(square2(7))
print(add(3,10))