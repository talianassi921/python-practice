# *args - special operator youc an pass to functions, gathers remaining arguments as a tuple
# args is a tuple of all the arguments

def sum_all_nums(*args):
    total = 0
    for num in args:
        total +=num
    return total 

print(sum_all_nums(4,6))
print(sum_all_nums(5,1,4))

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"

    return "Not sure who you are..."

ensure_correct_info() # Not sure who you are...

ensure_correct_info(1, True, "Steele", "Colt")