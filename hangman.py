import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'programming', 'game', 'code']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")
            if attempts == 0:
                print("You ran out of attempts! The word was:", word_to_guess)
                break
        else:
            print("Good guess!")

            if all(letter in guessed_letters for letter in word_to_guess):
                print("Congratulations! You guessed the word:", word_to_guess)
                break

hangman()

