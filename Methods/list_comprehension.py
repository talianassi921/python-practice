nums = [1,2,3]
new_nums = [x*10 for x in nums]
print(new_nums)

colors = ["red", "orange", "yellow"]
new_colors = [color.upper() for color in colors]
print(new_colors)

numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens)
print(odds)

list = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(list)