import random

print("Welcome to the guessing Game!")
a = eval(input('Please type in a number!'))
b = random.randint(0 ,100)
times = 0

while True:

 if a != b:
    print("wrong")
    a = eval(input('Please type in a number!'))
    times = times + 1
 elif a == b:
        print("you won after ", times, " guesses.")









