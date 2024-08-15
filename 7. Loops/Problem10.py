#print multiplication table of n using for loop in reversed order
n=int(input("enter the value of n "))
for i in range(10,0,-1):
    print(f"{n} * {i} = {n*i}")