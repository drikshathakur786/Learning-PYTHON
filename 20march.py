line = 'The quick brown fox jumps over the lazy dog'
# Pangram - if has all letters from a to z
# else- Not a pangram 
# Use sets

# line = input("Enter:").lower()

#line = line.lower()
#a = set(line)
#a.remove('')
#if len(a)==26:
#    print('Pangram')
#else:
#    print('Not a Pangram')


vowel = [ ]
consonant = [ ]
for i in line:
    if i.isalpha():
        if i in 'aeiou':
            vowel.append(i)
        else:
            consonant.append()
print(vowel)
print(consonant)


