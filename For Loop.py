count=1
while count <=10:
    print(count)
    count=count+1

# Using for loop:
# count is a variable
# in for loop one line multiple tasks
    
# Will print One less than given range
for count in range (1,10):
    print(count)
# if range(11) no start then it will by default start with 0
# range (1,30,2) - 2 is the step size

for count in range(1,11):
    print(f'{5} x {count} = {count*5}')

# Finding factorial using for loop
# as range is upto 5 so the factorial of 5 will be printed

fact = 1
for count in range(1,6):
    fact *= count
print('Factorial:',fact)

# Prime number program:
num=7
for i in range(2,num):
    if num%i==0:
        print('Not Prime')
        break
else:
    print('prime')

# Time complexity is more for this code
num=10
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        print('Not Prime')
        break
if is_prime==True:
    print('prime')

# How many even number that are prime- Only 2
# Then why are we checking?
num=4

if num==2:
    print('Prime')
elif num%2==0:
    print('Not Prime')
else:
    is_prime=True


    for i in range(3,num,2):
        if num%i==0:
            is_prime=False
            print('Not Prime')
            break

    if is_prime==True:
        print('prime')

# Change this program You have to print all the prime numbers from 1-100 by modifying this code.





