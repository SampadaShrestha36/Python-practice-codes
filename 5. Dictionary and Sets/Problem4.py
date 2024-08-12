#show that though same value is used, the datatype defines the length of the set but not in case of floating point and int values
s=set()
s.add("20")
s.add(20)
s.add(20.0) #20=20.0 in python
print(len(s))