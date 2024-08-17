#Write a python function to remove a given word from a list ad strip it at the same time.
def stri(l1,s):
    l=[]
    for item in l1:
        l.append(item.strip(s))
    return l
l1=["#hello","##hello world##","nothing#"]
print(stri(l1,"#"))