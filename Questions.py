# Write a program that takes a user's name as input and prints a personalized greeting.
# If the name starts with a vowel, the program should print "Hello, [name]! You have a special name!" 
# If the name starts with a consonant, it should print "Hello, [name]! Nice to meet you!"
# Additionally, if the name contains more than 5 letters, it should print "By the way, that's a long name!"
name= input("Enter your name:")
if name[0].lower() in 'aeiou':
    print("Hello" +name+ "! You have a special name!")
else:
    print("Hello" +name +"! Nice to meet you!")

if len(name) > 5:
    print("By the way, that's a long name!")

# Write a program that takes a year as input and determines if it is a leap year or not.
# A leap year is a year that is divisible by 4 but not divisible by 100, except for years that are divisible by 400. 
# Your program should display whether the given year is a leap year or not.
year= int(input("Enter a year:"))
if (year%4== 0 and year%100!=0) or (year%400==0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Write a program that takes a user's favorite color as input and determines if it is a warm color or a cool color. 
# Consider warm colors to be red, orange, and yellow, and cool colors to be blue, green, and purple.
# Your program should display whether the user's favorite color is warm or cool  
color= input("Enter your favorite color:")
color = color.lower()
if color in ['red','orange','yellow']:
    print("Your favorite color",color, "is a warm color.")
elif color in ['blue', 'green', 'purple']:
    print("Your favorite color",color, "is a cool color.")
else:
    print("Error")

# Write a program to display last digit of inputed number by user{ example:  if user enter a 4567 number then you have to fetch last digit "7" and then show 7 as output}
n = int(input("Enter a number:"))
lastdigit = n%10
print(lastdigit)

# Write a program to check whether a person is senior citizen or not?( person equal or more than 60 years old is categorised as senior citizen)
age= int(input("Enter your age:"))
if age >= 60:
    print("Senior citizen.")
else:
    print("Not a senior citizen yet.")

# To check whether a inputted number is positive or negative
n= float(input("Enter a number: "))
if n>0:
    print("POSITIVE")
elif n<0:
    print("NEGATIVE")
else:
    print("ZERO")

# Write a program to check whether the entered character is vowel or not
char = input("Enter a character: ").lower()
if char in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Not a vowel.")

# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
# Tax-Cost price (in Rs)
# 15 %- > 100000
# 10% - > 50000 and <= 100000
# 5%- <= 50000
cp= float(input("Enter the cost price of the bike (in Rs): "))
if cp>100000:
    tax= 0.15*cp
elif cp>50000 and cp<=100000:
    tax= 0.10*cp
else:
    tax= 0.05*cp
print("The road tax to be paid for the bike is Rs",tax)


