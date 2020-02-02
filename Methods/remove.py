#remove the first item from the list whos value is x
list = [1,2,3,4,4,4]
list.remove(2)
print(list) #[1,3,4,4,4]
list.remove(4) #if more than 1, it just removes the first one
print(list) # [1,3,4,4]