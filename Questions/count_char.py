def count_char(char, word):
    return [word.count(char) for char in word if char in "o"]

print(count_char("o", "computer"))