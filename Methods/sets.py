#no duplicate values
#elements in set are not ordered
#you can not access items in a set by index

# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

4 in s
# True

8 in s
# False


numbers = {1,2,3,4}

for number in numbers:
    print(number)

# 1
# 2
# 3
# 4

cities = ["Los Angeles", "San Diego", "Los Angeles", "Miami"]
print(set(cities)) #turns a list into a set