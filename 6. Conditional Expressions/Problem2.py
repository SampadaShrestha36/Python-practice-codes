#calculate pass or failed by taking marks as input
m1=int(input("enter the marks in subject1"))
m2=int(input("enter the marks in subject2"))
m3=int(input("enter the marks in subject3"))
t=int(input("enter full marks"))
percentage1=(m1/t)*100
percentage2=(m2/t)*100
percentage3=(m3/t)*100
totalpercentage=((m1+m2+m3)/(3*t))*100
if(percentage1>=33 and percentage2>=33 and percentage3>=33 and totalpercentage>=40):
    print("You have passed with total percentage ", totalpercentage)
else:
    print("You have failed with total percentage ", totalpercentage)
