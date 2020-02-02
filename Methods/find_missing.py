def find_missing(list1, list2):
    return [x for x in list1 if x not in list2]

print(find_missing([1,2,3,4,5],[2,3,4,5]))