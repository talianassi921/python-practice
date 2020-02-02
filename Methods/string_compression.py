def string_compression(string):
    return ''.join(set([x+str(string.count(x)) for x in string]))
    
print(string_compression("talia"))