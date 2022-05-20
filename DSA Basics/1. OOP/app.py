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
'''
class Dog:
    def bark(self):
        print("bark")

d = Dog()
d.bark() # output --> bark
print(type(d)) # output --> <class '__main__.Dog'>