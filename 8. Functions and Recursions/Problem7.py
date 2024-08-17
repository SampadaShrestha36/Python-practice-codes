#print fibonaccii series using recursive function
def fib(n,a,b,c):
    if(n<=1):
        return
    else:
        c=a+b
        a=b
        b=c
        print(f"{c}\t",end="")
        return fib(n-1,a,b,c)
n=int(input("enter a number"))
a=0
b=1
c=0
print(f"{a}\t{b}\t", end="")
fib(n-2,a,b,c)