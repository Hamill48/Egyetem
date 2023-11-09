import random

while True:
    randomNumber = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input('Write a number to guess: '))
        if guess > randomNumber:
            print("It's smaller than your guess!")
            attempts += 1
            continue
        elif guess < randomNumber:
            print("It's bigger than your guess!")
            attempts += 1
            continue
        elif guess == randomNumber:
            print(f"Congratulations! You have guessed it in {attempts} guesses!")
            break
    
    doCountinue = input('Do you want to play again? ')

    if doCountinue == 'yes':
        attempts = 0
        continue
    elif doCountinue == 'no':
        break