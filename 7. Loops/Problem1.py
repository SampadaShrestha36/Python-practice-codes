#print the multiplication table of a given number using for loop
a=int(input("enter the number"))
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")