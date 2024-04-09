# TASK- Animals = No. of tasks
# Have to write some common things in all classes
# If change in all classes? Then its a long process
# keep a common message - 'We are animals and we love humans'
# Manually you can input this in limited no. of classes
# So we use inheritance


# Parent class
class Animal():
    eyes = 2
    legs = 4
    tail = 1

    def mssg(self):
        print('We are animals and we love humans')

# Child class
class Dog(Animal):
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def speak(self):
        print("Woof Woof")

class Cat(Animal):
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def speak(self):
        print("Meow Meow")

class Lion(Animal):
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def speak(self):
        print("Roarrrr")

tommy = Dog('Tommy',2,'Black')
tom = Cat('Tom',2,'Cartoon')
jerry = Lion('Jerry',1,'Cartoon')

tom.speak()
tommy.speak()
jerry.speak()

# use inherentence to use animal class
