with open('paragraph.txt','r') as my_file:
    text= my_file.read()
for word in (text.split()):
# for printing all number    
#    if word.isnumeric():
#        print(word)
    if word.isnumeric() and len(word)==10:
        print(word)

# Decorators- type of function.. increase the functionality of some function
#
def guruji(banda):
    def shaktimaan():
        banda()
        print("Mai hee hu shaktimaan")
    return shaktimaan
def gangadhar():
    print('Namaste me hu gangadhar')

shakti = guruji(gangadhar)
shakti()
# gangadhar()

# OOPS
