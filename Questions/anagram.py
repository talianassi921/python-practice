def isAnagram(string1, string2):
    new_string1 = string1.replace(" ", "")
    new_string2 = string2.replace(" ", "")
    return sorted(new_string1) == sorted(new_string2)
    
    
print(isAnagram("cat", "tac"))
print(isAnagram("p ie", "pie"))
print(isAnagram("clint eastwood", "old west action"))
print(isAnagram("mug", "dog"))
print(isAnagram("Tall", "laTl"))



