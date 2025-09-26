#hi 
class Greet:
    def __init__(self, str):
        self.str = str
    def hello(self):
        print(self.str)

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        print(self.a + self.b)

number = Calc(5, 10)
number.addition()

greet = Greet("Hiiiiii")
greet.hello()