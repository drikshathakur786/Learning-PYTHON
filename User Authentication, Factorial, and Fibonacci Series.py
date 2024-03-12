username = input('Enter your username:')
password = input('Enter your password:')

# generally flag is used so you can also write flag='red
# Method 1:
signal='red'
while signal=='red':
    if username=='abc' and password=='123@123':
        print('login')
        signal='green'
    else:
        print('Galat hai!!')
        username = input('Enter your username:')
        password = input('Enter your password:')

# Method 2:
# break- works in loop. Wherever break is detected by the compiler it immediately comes out of the loop
while True:
    if username=='abc' and password=='123@123':
        print('login')

    else:
        print('Galat hai!!')
        username = input('Enter your username:')
        password = input('Enter your password:')

# Find the factorial of a number
# number= int(input('Enter any number:'))
# # !4= 4x3x2x1
# # 4!= 1x2x3x4
fact=1
count=1

while count<=number:
    fact= count*fact
    count= count + 1
print('Factorial of a number is:',fact)

# Mostly asked in interviews
# Fibonacci Series
# Start 2 digits fixed 0 1
# 0 1 1 2 3 5 8 13
# Print only till 8

a,b = 0,1
print(a)
print(b)
while True:
    c= a+b
    if c>8:
        break
    print(c)
    a,b = b,c

# Alternative:
number= int(input('Enter any number:'))
num1=0
num2=0
count=3
print(num1,num2,end='')
while count<=8:
    next=num1+num2
    print(next,end='')
    num1=num2
    num2=next
    count=count+1

