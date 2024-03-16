cars=['Ford','BMW','Nissan','Toyota']
print(cars)

# Want to print like:
# Ford
# BMW
# Nisaan
# Toyota

# For now:
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])

for i in range (4):
    print(cars[i])

# Ques you have a list
numbers=[1,2,3,4,5,6,7]
# Sum of all numbers in list
sum = 0

# Without range
for num in numbers:
    sum = sum + num
print(sum)

# With range
for i in range(7):
    sum = sum + numbers[i]
print(sum)







