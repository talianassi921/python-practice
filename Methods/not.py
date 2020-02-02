print("How old are you?")
age = int(input())
if not ((age >= 2 and age <=8) or age >=65):
    print ("you pay $10")
else:
    print("you are a child or senior")