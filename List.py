cars= "Ford, Tata, Nissan, Range"
print(cars)

cars2= ['NANO','ALTO','AUTO0']
cars.extend(cars2)
print(cars)
#or
cars= cars+cars2

#What if you want to print nissan only 

# Lists:
cars = ['Ford', 'Mustang', 'Tata', 'Toyota','Nissan', 'BMW']

# Printing only Toyo from toyota using slicing
print(cars[3][:4])

# Printing in reverse order
print(cars[::-1])

# Printing only Mustang, Tata, Toyota
print(cars[1:4])

# always append at last
cars.append('Nano')
print(cars)

# always delete from last
cars.pop()
print(cars)

# return
a = cars.pop()
print(cars,a)

# if you dont give index number it deletes the last item
# a = cars.pop(1)

# what if you dont remember the index number of BMW but you want to remove it?

# pop= based upon index number, remove= using item name
cars.remove('Nishan')
print(cars)

# what if you want to add on a position
cars.insert(2,'Swift')
print(cars)

# What if you want to remove toyo
a= cars[3][:4]
cars.remove('Toyota')
cars.insert(3,a)
print(cars)

# count
cars= cars.count('Ford')
print(cars)

# cars = cars.index('Tata')
# print(cars)

# if lists contain only alphabets or only no. then only sorting possible
#cars.sort(reverse=True)
#print(cars)

# What is the difference between append and extend



