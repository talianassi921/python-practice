def max_even(numbers):
    return max([num for num in numbers if num % 2 == 0])

print(max_even([2,3,7,8,10,40]))
print(max_even([1,3,5,6,21]))