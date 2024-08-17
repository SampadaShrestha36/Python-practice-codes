#create function to convert celsius to fahrenheit
def converter(c):
    f=(c*(9/5))+32
    return f
c=int(input("enter temperature in celsius"))
f=converter(c)
print("The temperature in fahrenheit is ",f)
