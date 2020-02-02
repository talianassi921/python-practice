set = {x**2 for x in range(10)}
print(set)

set2 = {char.upper() for char in "hello"}
print(set2)

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) ==5

string = "hello"
