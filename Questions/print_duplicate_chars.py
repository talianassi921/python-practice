def print_duplicate_chars(string):
    count = {}
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for key in count:
        if count[key] > 1:
            print([key, count[key]])

print_duplicate_chars("talia")
print_duplicate_chars("chocolate")