def binary_search(ints, target):
    low = 0
    high = len(ints) - 1
    while low <= high:
        mid = (low + high) // 2
        if ints[mid] == target:
            return True
        elif ints[mid] > target:
            high = mid - 1
        else: 
            low = mid + 1
    return False
            
print(binary_search([10, 20, 50, 100, 350, 1000], 10001))
        
        