def find_missing(ints):
    return [x for x in range(ints[0], ints[-1]+1) if x not in ints]

print(find_missing([1,2,3,5,6]))
print(find_missing([10,11,12,15,16]))