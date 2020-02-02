def isPalindrome(string):
    new_string =  "".join([letter.lower() for letter in string if letter.isalnum()])
    return new_string == new_string[::-1]

print(isPalindrome("racecar"))
print(isPalindrome("A man, a plan, a canal: Panama"))