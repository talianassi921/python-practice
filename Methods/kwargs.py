#gathers remaining keyword arguments in a dictionary

# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s faborite color is {color}")

    
# fav_colors(colt="purple", talia="pink")

def special_greeting (**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is..."

print(special_greeting(David='Hello'))
print(special_greeting(Bob='hello'))
print(special_greeting(David='special'))