# 9653329826
# You want to convert this in binary
# Convert decimal no. to binary

# Method 1:
num=100
ans=0
while ans!=1:
    ans = num//2
    remainder =  num%2
    num = ans
    print(remainder)
print(ans)

# Method 2:
num=100
ans=0
binary = ''
while ans!=1:
    ans = num//2
    remainder =  num%2
    num = ans
    binary = str(remainder) + binary
print('1'+binary)


cars = 'BMW Ford Mustang Nissan Toyota'.split()
print(cars)

# You want to remove duplicay. How?

cars=['BMW', 'Ford', 'Mustang', 'Nissan', 'Toyota','Nissan','Mustang','BMW']
# Using typecasting you can remove duplicacy

cars=list(set(cars))
print(cars)

# Sets:
# No duplicate values allowed
# No indexing
# Hashing used
cars={'BMW', 'Ford', 'Mustang', 'Nishan', 'Toyota','Nishan','Mustang','BMW'}

cars.pop()
cars.remove('Ford')
print(cars)

# Hashing in simple terms is like putting things in different boxes based on their characteristics.
# In Python, you can think of sets as boxes, and hashing is the process of determining which box an item belongs to based on its unique characteristics, called a hash value. 

