import random

number = random.randint(1,10)
print("Guess a number between 1 and 10")
guess = int(input())
while guess != number:
    if guess<number:
        print("Too low, try again!")
        guess = int(input())
    if guess>number:
        print("Too high, try again!")
        guess = int(input())
print("You guessed it! You won!")