#write a class "calculator" capable of finding square,cube and square root of a number
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
print("enter your choice:")
print("1.square 2.cube 3.sqrt")
i=int(input())
n=int(input("enter the number"))
a=calculator(n)
match i:
    case 1:
        print(a.square())
    case 2:
        print(a.cube())
    case 3:
        print(a.squareroot())
    case other:
        print("Invalid choice!")
