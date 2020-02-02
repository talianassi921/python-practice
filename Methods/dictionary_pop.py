#takes a single argument (key) of what you want to remove

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "favorite_language": "Python"
}

instructor.pop("owns_dog")
print(instructor)