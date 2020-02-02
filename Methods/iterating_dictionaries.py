instructor = {
    "name": "Colt",
    "owns_dog": True,
    "favorite_language": "Python"
}

# to check if a key is in the dictionary
print("name" in instructor) # true

#to check if a value is in the dictionary
print(True in instructor.values()) # true

# # access only values
# for value in instructor.values():
#     print(value)
    
# # access only keys
# for keys in instructor.keys():
#     print(keys)
    
#access values and keys
# for key,value in instructor.items():
#     print(f"{key}: {value}")