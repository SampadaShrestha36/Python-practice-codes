#changing self parameter inside a class to something else
class programmer:
    company="microsoft"
    def setname(slf,name):  #no change 
        slf.name=name
    def setsalary(sf,salary):   #no change
        sf.salary=salary
p1=programmer()
a=input("enter the name")
p1.setname(a)
b=int(input("enter the salary"))
p1.setsalary(b) 
print("The name, salary and company are",p1.name,p1.salary,p1.company)