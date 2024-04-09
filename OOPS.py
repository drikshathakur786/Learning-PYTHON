# object oriented programming language (OOPs)
# class- blueprint/ constructor

# Creating a clas
class heyBruh:
    x=5

# we can use this class to create objects
y= heyBruh
print(y.x)

# __init__() : inbuilt function
#  to assign values for name and age

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Driksha",18)
print(p1.name)
print(p1.age)

# camel casing- first letter of word is captial
class Car():
# Properties of car
    name = 'Ford'
    model = 'Mustang'
    top_speed = 200
    doors = 2
    tyres = 4
    color = 'black'

    def start(self):
        print('Vrom Vrom')

# car class object
car1 = Car()
print(car1.color,car1.model)
car1.start()

# make dog class and write some properties
class Dog():
# attributes
    name = 'Bruno'
    breed = 'Golden Retriever'
    age = 3
    color = 'Golden'
# methods
    def bark(self):
        print('Woof! Woof!')

dog1 = Dog()
print(dog1.name, dog1.breed, dog1.age, dog1.color)
dog1.bark()





