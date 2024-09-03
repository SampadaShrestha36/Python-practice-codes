#create a class train to book a ticket, get fare information, get status of train
class Train:
    def book(self,train_no, fro, to,seats):
        print(f"the train no:{train_no}, has booked {seats} seats for travel from {fro} to {to}")
    def fare(self,train_no,seats,fare):
        print(f"The train fare of train no: {train_no} for {seats} number of seats is {fare}")
    def status(self,train_no, fro,to):
        print(f"The train from {fro} to {to} with train number: {train_no} is arriving on time")
t1=Train()
t1.book(112,"ktm","bkt",2)
t1.fare(112,2,5000)
t1.status(112,"ktm","bkt")