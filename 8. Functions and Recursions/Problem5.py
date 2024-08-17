#Write a python function which converts inches to cms
def converter(i):
    c=(i*2.54)
    return c
i=int(input("enter length in inches"))
c=converter(i)
print("The length in cm is ",c)
