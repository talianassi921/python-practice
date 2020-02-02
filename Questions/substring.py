def substring(string, substring):
    if len(substring) > len(string):
        return False
    
    count = {}
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for char in substring:
        if count[char] >= 1:
            count[letter] -= 1
        else:
            return False
        return True
    
print(substring("bookend", "book"))
print(substring("hulu", "hulugans"))
print(substring("hulugans", "hulu"))
