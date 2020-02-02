def max_odd(numbers):
    return max([x for x in numbers if x % 2 != 0])

print(max_odd([3,4,6,7,8,9]))
print(max_odd([0,3,57,101]))