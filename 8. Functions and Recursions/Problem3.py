#write recusive function to find sum of first n natural numbers
def rsum(n):
    if(n<=1):
        return 1
    else:
        return (n+rsum(n-1))
n=int(input("enter the number"))
s= rsum(n)
print("the sum is", rsum(5))
