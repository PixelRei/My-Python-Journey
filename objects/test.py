#hi 
class Greet:
    def __init__(self, str):
        self.str = str
    def hello(self):
        print(self.str)


#there are three methods in a class that we use the most:
#1. __init_ method: it is a constructor that initializes the object
#2. __str__ method: it is used to return a string representation of the object
#3. __repr__ method: it is used to return a string with the object type and more informations
class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        print(self.a + self.b)
    @staticmethod #if you want to create a static method in a class
    def addNumbers(a, b):
        print(a + b)

number = Calc(5, 10)
number.addition()
number.addNumbers(20, 30)

greet = Greet("Hiiiiii")
greet.hello()