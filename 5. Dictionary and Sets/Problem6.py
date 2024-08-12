#an example of dictionary
d={}
s=input("enter name of the person")
t=input("enter the favourite language")
d.update({s:t})
s=input("enter name of the person")
t=input("enter the favourite language")
d.update({s:t})
s=input("enter name of the person")
t=input("enter the favourite language")
d.update({s:t})
s=input("enter name of the person")
t=input("enter the favourite language")
d.update({s:t})
print(d)
#if two keys are same then only the recent update will be taken
#if two values are same then the keys are still different so it does not matter. It will be considered as separate element