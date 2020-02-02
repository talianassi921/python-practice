# numbers = (1,2,3,4)
# #when you define a tuple you can not change it (its immutable)
# tuples can be keys, lists can not

# 3 in numbers # true

# alphabet = ('a', 'b', 'c', 'd')
# print(type(alphabet))
# alphabet[0]='A' #error because you can't change values of a tuple
# print(alphabet)

# first_tuple = (1, 2, 3, 3, 3)

# first_tuple[1] // 2
# first_tuple[2] // 3
# first_tuple[-1] // 3

# second_tuple = tuple(5, 1, 2)

# second_tuple[0] # 5
# second_tuple[-1] # 2

locations = {
    (35.68, 39.69): "Tokyo Office",
    (40.71, 74.00): "New York Office",
    (37.77, 122.41): "San Francisco Office"
}

locations[(37.77, 122.41)] # "San Francisco Office"