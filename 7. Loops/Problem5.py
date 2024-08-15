#sum of first n natural numbers using while loop
i=1
s=0
n=int(input("enter the number"))
while(i<=n):
    s=s+i
    i+=1
print("the sum is", s)