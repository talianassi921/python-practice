def unique_chars(string):
    for x in string:
        if string.count(x)>1:
            return False
    return True

print(unique_chars("talia"))
print(unique_chars("Henry"))
print(unique_chars("Ttalia"))