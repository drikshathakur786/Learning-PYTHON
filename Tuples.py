# Converting String to list
cars="BMW Ford Mustang Range Nissan".split()
print (cars)

# Tuple: similar to list
cars= ('BMW','Ford','Mustang','Range','Nissan')

# Difference: tuples are not mutable(not-changeable) while lists are mutable(changeable).

cars= ['BMW','Ford','Mustang','Toyota','Range','Nissan']
cars[3]='Toyo'
print(cars)

# Strings cannot be directly changed. Hence, strings are also not mutable.

# name='Driksha Thakur'
# name[3]='h'
# print(name)

cars= ('BMW','Ford','Mustang','Toyota','Range','Nissan')
# cars[3]='Toyo'

# How to  make change in tuple:
x=list(cars)
print(x)
x[3]='Toyo'
cars=tuple(x)
print(cars)





