# Guess the number game

import random

random_number = random.randint(1,100)
remaining_chances = 10

# eg the no. is 44
# Your guess is less than my number
# Your guess is more than my number

# 10 chances only

while remaining_chances > 0:
    user_guess = int(input('Enter Your Guess:'))

    if user_guess == random_number:
        print('---Badhai ho bhai---')
        break
    elif user_guess < random_number:
        print('---Thoda Kamm hai---')
    elif user_guess > random_number:
        print('---Bohot jada hai---')
        

# Convert into 10 chances
# Print tumse na ho payega and also tell how many chances left
    remaining_chances -= 1
    print('Chances left:',remaining_chances)

if remaining_chances == 0:
    print('Tumse na ho payega ')



