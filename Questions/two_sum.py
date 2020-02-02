def twoSum(nums, target):
    for x in nums:
        if target-x in nums and nums.indexOf(x) != nums.indexOf(target-x):
            return [x, target-x]
        else:
            index += 1
    return "Not found"

print(twoSum([3,2,4], 6))