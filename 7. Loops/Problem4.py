#find out whether a number is prime or not
a=int(input("enter a number"))
for i in range(2,a):
    if(a%i==0):
        print("It is not prime number")
        break
else:
    print("It is a prime number")