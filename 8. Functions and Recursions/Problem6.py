#Write a python function to print multiplication table of a given number.
def multi(n,i):
    if(i>10):
        return
    else:
        print(f"{n} * {i} = {n*i}")
        return multi(n,i+1)
n=int(input("enter a number"))
multi(n,1)
