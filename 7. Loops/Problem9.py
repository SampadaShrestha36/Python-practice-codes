''' print the followig star pattern
***
* *
***
   '''
n=int(input("enter the value of n"))
for i in range(1,n+1):
    if (i%2==0):
        print("*",end="")
        print(" "*(n-2), end="")
        print("*")
    else:
        print("*"* (n))