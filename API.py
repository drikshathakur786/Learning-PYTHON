# use 'pip install requests'- command to use requests (importing the Requests library)
# Requests is a popular HTTP library for making HTTP requests in Python.
# provides an easy-to-use and intuitive API for sending HTTP requests and handling responses

# https://sv443.net/jokeapi/v2/

import requests

raw_data=requests.get('https://v2.jokeapi.dev/joke/Spooky')

jokes=raw_data.json()

print(jokes)

if jokes['type']=='single':
    print(jokes['joke'])
else:
    print('Ques:',jokes['setup'])
    print('Ans:',jokes['delivery'])


# Homework:
# Set the amount of jokes 
# link will be updated, copy , paste - data changed
# observe the change in json data
# now you want to print all the jokes together, how?
    
# rapid api

import requests

raw_data = requests.get('https://v2.jokeapi.dev/joke/Any?amount=10')
jokes= raw_data.json()

jokes= jokes["jokes"]

all_jokes = []

for joke in jokes:
    if joke.get('setup') and joke.get('delivery'):
        all_jokes.append(joke['setup'])
        all_jokes.append(joke['delivery'])
    elif joke.get('joke'):
        all_jokes.append(joke['joke'])

print("\n".join(all_jokes))