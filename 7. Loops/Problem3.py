#print the multiplication table of a given number using while loop
a=int(input("enter the number"))
i=1
while (i<=10):
    print(f"{a} * {i} = {a*i}")
    i+=1