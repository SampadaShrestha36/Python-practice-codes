#calculate grade from marks of the student
a=int(input("enter the marks"))
if(a<=100 and a>90):
    print("Ex")
elif(a<=90 and a>80):
    print("A")
elif(a<=80 and a>70):
    print("B")
elif(a<=70 and a>60):
    print("C")
elif(a<=60 and a>70):
    print("D")
else:
    print("Failed")