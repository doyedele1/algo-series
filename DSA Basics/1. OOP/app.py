'''
    Introduction to Object-Oriented Programming in Python
        x = "hello"
        print(type(x)) # output --> <class str>
            x is the object of the class string

        def hello():
            print("hello")
        print(type(hello)) # output --> <class function>

        Methods
        string = "hello"
        print(string.upper())
            upper() is the method for class string
'''

'''
    Creating our defined (blueprint) classes
        - A method is a function that goes inside a class
        - d is the instance of the class Dog. d is the object of type Dog

        - __init__ is a special method in Python that helps to instantiate the object right when it is created
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name)

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Nymeria", 12) # to understand what __init__ does
print(d.name) # Nymeria
print(d.get_age()) # 12
d.set_age(10)
print(d.get_age(10)) # age is now 10

d2 = Dog("Summer", 5) # to understand what self does in __init__
print(d2.name) # Summer
d.bark() # output --> bark
print(d.add_one(5)) # output --> 6
print(type(d)) # output --> <class '__main__.Dog'>