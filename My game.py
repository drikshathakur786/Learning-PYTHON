import random

print('Welcome to the Rock, Paper, Scissors game!')

choices = ['Stone', 'Paper', 'Scissor']

user_choice = input('Enter Stone, Paper, or Scissor: ').capitalize()
computer_choice = random.choice(choices)

print(f"Computer's choice: {computer_choice}")

if user_choice == computer_choice:
    print('--------------Tie---------------')
elif (user_choice == 'Stone' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Scissor') or (user_choice == 'Scissor' and computer_choice == 'Stone'):
    print('-------Computer Won------------')
else:
    print('----------You Won---------------')

print(f"Your choice: {user_choice}")

