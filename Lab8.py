class Dog:
    pass

d1 = Dog()
d2 = Dog()

print(d1)
print(d2)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d1 = Dog("Buddy", 3)
print(d1.name)
print(d1.age)

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says Woof!")

d1 = Dog("Buddy")
d1.bark()

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
    
c = Calculator()
print(c.add(2, 3))
print(c.multiply(4, 5))

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
    def display(self):
        print(self.owner, "has", self.balance)

acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.display()

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def display(self):
        print("Count:", self.count)

c = Counter()
c.increment()
c.increment()
c.display()

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10    
    
    def brake(self):
        self.speed -= 5

    def display(self):
        print(self.brand, "speed: ", self.speed)

c1 = Car("Toyota", 50)
c1.accelerate()
c1.display()

# What is a class?

# A class is like a blueprint or template 
# for creating objects. It defines what data 
# (attributes) and actions (methods) something 
# will have.

# What is an object?

# An object is an instance of a class

# What is a method?

# A method is a function that is defined inside a class and 
# can be called on objects of that class.

# How does state change in objects?

# State changes in objects when methods are called
#  on them, which modify the values of their attributes.
