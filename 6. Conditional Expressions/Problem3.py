#detect a spam comment
a=input("enter the comment")
if(("Make a lot of money" in a) or("Buy now" in a) or("Subscribe this" in a) or ("click this" in a)):
    print("It is a spam comment")
else:
    print("It is not a spam comment")