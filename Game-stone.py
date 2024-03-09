# User input- stone/paper/scissor
# Computer will also choose. how will this happen?
# choices= ['Stone','Paper','Scissor']
# print(choices[0])
# You want that randomly one number should come from range 0-2
# if same then tie rest conditions

import random
print('Welcome to our game')
random_index = random.randint(0,2)
choices= ['Stone','Paper','Scissor']
computer_choice = choices[random_index]
user_choice=input('Enter Stone, Paper or Scissor:')
user_choice = user_choice.lower()

if user_choice == computer_choice:
    print('--------------Tie---------------')
elif user_choice == 'Stone' and computer_choice == 'Paper':
    print('-------Computer Won------------')
elif user_choice == 'Stone' and computer_choice == 'Scissor':
    print('----------You Won---------------')
elif user_choice == 'Paper' and computer_choice == 'Stone':
    print('--------You Won------------')
elif user_choice == 'Paper' and computer_choice == 'Scissor':
    print('----------Computer Won------')
elif user_choice == 'Scissor' and computer_choice == 'Stone':
    print('----------Computer Won------')
elif user_choice == 'Scissor' and computer_choice == 'Paper':
    print('--------You Won------------')

print(f"Your choice: {user_choice}")
print(f"Computer's choice: {computer_choice}")
