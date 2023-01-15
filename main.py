import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a Number between 1 and {x}: '))
        if guess < random_number:
            print(f'higher ')
        elif guess > random_number:
            print(f'lower ')
        # elif guess == random_number:
        #     print(f'correct, {random_number}! ')
    print(f'correct, {random_number}')
    
guess(10)