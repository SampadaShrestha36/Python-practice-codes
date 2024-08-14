#find if a username contains less than 10 characters or not
a=input("enter username")
b=len(a)
if(b<10):
    print("username contains less than 10 characters")
else:
    print("username contains more than 10 characters")