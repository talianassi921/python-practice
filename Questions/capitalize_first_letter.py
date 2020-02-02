def capitalize_first_letter(sentence):
    return " ".join([x[0].upper()+x[1:] for x in sentence.split(" ")])

print(capitalize_first_letter("talia is really cool"))