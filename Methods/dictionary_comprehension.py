numbers = dict(first=1, second=2, third=3)

squared_numbers = {key:value ** 2 for key,value in numbers.items()}

print(squared_numbers)


new_dictionary = {num: num**2 for num in range(1,6)}

print(new_dictionary)


string1="ABC"
string2="123"
combo = {string1[i]:string2[i] for i in range (0,len(string1))}
print(combo)

instructor={'name': 'colt', 'city': 'san fran', 'color': 'purple'}
yelling_instructor= {k.upper():v.upper() for k,v in instructor.items()}
print(yelling_instructor)

num_list = [1,2,3,4]
new_num_list = {num:("even" if num % 2 == 0 else "odd") for num in range(1,5)}
print(new_num_list)