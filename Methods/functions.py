def say_hi():
    print('Hi!')
    
say_hi()
# Hi

def square(num):
    return num**2

print(square(4))

def sing_happy_birthday(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday to you")
    
sing_happy_birthday("Talia")

def add(a,b):
    return a+b

print(add(6,5))

def multiply(a,b):
    return a*b
print(multiply(5,7))

#sets the default to 2 if there is no argument passed in for power
def exponent(num,power=2):
    return num ** power
print(exponent(2,3))