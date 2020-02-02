#finds index of an item in a list
numbers = [5,6,7,8,9,10]
print(numbers.index(6)) #returns the index of 6

#can specify a start and end
list = [5,5,6,7,5,8,8,9,10]
print(list.index(5,1)) #1
print(list.index(5,2)) #4
print(list.index(8,6,8)) #looks for 8 between indexes 6 and 8
