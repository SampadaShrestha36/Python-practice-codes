#create function to find the greatest of three numbers
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
g=greatest(a,b,c)
print(g, "is the greatest")