#create a class "programmer" and store information of person working at Microsoft
class programmer:
    company="microsoft"
    def setname(self,name):
        self.name=name
    def setsalary(self,salary):
        self.salary=salary
p1=programmer()
a=input("enter the name")
p1.setname(a)
b=int(input("enter the salary"))
p1.setsalary(b) 
print("The name, salary and company are",p1.name,p1.salary,p1.company)