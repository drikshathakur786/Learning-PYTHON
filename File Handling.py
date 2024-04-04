my_cow=open('My cow.txt','r')
# Read, Write, Append - MODES

#print(my_cow.read())

# Can save in variable also:
text = my_cow.read()
print(text)

text = my_cow.readline()
print(text)

# Overwrite
my_cow = open('new.txt','w')
my_cow.write('I am fine')

# w- overwrite, x- gives error
#my_cow = open('new.txt','x')
#my_cow.write('HEllo HEllo')

# append- to add lines
my_cow = open('new.txt','a')
my_cow.write('\nShe is black and white')


me = open("paragraph.txt", "r") 
paragraph = me.read()
print(paragraph)

phoneno = "9915081898"
if phoneno in paragraph:
    print(phoneno)
else:
    print("Not found")
