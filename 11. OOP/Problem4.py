#add a static method in problem 2, to greet the user with hello
import math
class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        return self.n**2
    def cube(self):
        return self.n**3
    def squareroot(self):
        return math.sqrt(n)
    @staticmethod
    def greetings():
        print("hello user")
print("enter your choice:")
print("1.square 2.cube 3.sqrt")
i=int(input())
n=int(input("enter the number"))
a=calculator(n)
match i:
    case 1:
        print(a.square())
        a.greetings()
    case 2:
        print(a.cube())
        a.greetings()
    case 3:
        print(a.squareroot())
        a.greetings()
    case other:
        print("Invalid choice!")
