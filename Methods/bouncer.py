print("How old are you?")
age = int(input())
if age:
    if age >=18 and age <21:
        print("You can enter but need a wristband")
    elif age>=21:
        print("You can enter and drink")
    else:
        print("You can not enter")
else:
    print("please enter an age")