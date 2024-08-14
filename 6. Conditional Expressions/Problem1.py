#Greatest of 4 numbers entered by the user
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
d=int(input("enter a number"))
if(a>b and a>c and a>d):
    print(f"{a} is the greatest")
elif(b>a and b>c and b>d):
    print(f"{b} is the greatest")
elif(c>a and c>b and c>d):
    print(f"{c} is the greatest")
else:
    print(f"{d} is the greatest")