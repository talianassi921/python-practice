def isPowerOfThree(num):
    if num == 0:
        return False
    while (num % 3 == 0 ):
        num /= 3
    return num == 1