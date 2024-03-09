# word = "mcdonald"
# x = word[0].capitalize()+ word[1] + word[2].capitalize() + word[3:]
# print(x) 
# word = word[:2].capitalize() + word[2:].capitalize() 
# print(word)

first_name= "Driksha"
last_name="Thakur"
# " " used to add space in first name and last name
full_name= first_name + " " +last_name
print(full_name)

word = input("Enter a word:") 
y = word[0].capitalize()+word[1]+word[2].capitalize()+word[3:] 
print(y)

# Write a code to swap two variables:
# Method 1:
a= int(input("Enter a:"))
b= int(input("Enter b:"))
c=a
a=b
b=c
print('a is:',a, 'and','b is:',b)

# Method 2:
a= int(input("Enter a:"))
b= int(input("Enter b:"))
a,b=b,a
print('a is:',a,'and','b is:',b)

# Method 3:
a= int(input("Enter a:"))
b= int(input("Enter b:"))
a= a+b
b= a-b
a= a-b
print('a is:',a,'and','b is:',b)







