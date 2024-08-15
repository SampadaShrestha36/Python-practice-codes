#calculate factorial of a given numebr using for loop
n=int(input("enter the number"))
f=1
for i in range(1,n+1):
    f=f*i
print("the factorial is", f)