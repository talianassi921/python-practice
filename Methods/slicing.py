# makes copies of lists or strings

# some_list[start:end:step]
# step = interval

first_list = [1,2,3,4]

first_list[1:] #2,3,4
first_list[-3:] # [2,3,4]

first_list[:2] #[1,2]
first_list[1:3] #[2,3]

first_list[:-1] # [1,2,3]

first_list[1::2] #[2,4]
first_list[::2] #[1,3]

colors = ["red", "yellow", "blue"]
colors[2][::-1] # eulb