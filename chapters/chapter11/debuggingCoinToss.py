import random

# 1) Bug Fix: 'toss' is an integer (0 or 1), while 'guess' is a string ('heads' or 'tails').
#    We need to convert 'toss' into a string ('heads' or 'tails') so we can compare correctly.

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()  # Accept uppercase inputs too

# Convert the integer toss into a string
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == 0:
    tossResult = 'tails'
else:
    tossResult = 'heads'

# 2) Bug Fix: Compare 'guess' (string) to 'tossResult' (string) instead of toss == guess
if guess == tossResult:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # 3) Bug Fix: The variable was spelled 'guesss' before. 
    #    Use the same variable name 'guess' to store second guess.
    guess = input().lower()

    # Compare again using the correct variable name
    if guess == tossResult:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
