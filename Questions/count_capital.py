def count_capital(string):
    return count([word for word in string if word[0].isupper()])

print(count_capital(["Talia", "book", "Computer"]))