import random

secretNum = random.randint(1, 20)
print('I\'m thinking of a number between 1 and 20.')
print('You get 6 tries.')
for guessesTaken in range(1, 6):
    print('Take a guess')
    guess = int(input())

    if guess < secretNum:
        print('Too low')
    elif guess > secretNum:
        print('Too high')
    else:
        break


if guess == secretNum:
    print('Good job! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The answer is ' + str(secretNum))
