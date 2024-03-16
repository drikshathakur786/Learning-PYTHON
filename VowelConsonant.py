# Check vowel or consonant. If entered a word- Error pls enter a single char. If entered a no. - Error pls enter a alphabet only
char = input("Enter:")
if len(char)==1:
    if char.isalpha():
        if char in 'aeiou':
            print('Vowel')
        else:
            print('Consonant')
    else:
        print('Please Enter a alphabet only.')
else:
    print('Please enter a single char only')
