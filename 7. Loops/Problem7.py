''' print the followig star pattern
     *
    ***
   ******
   '''
for i in range(1,4):
    print(" "* (3-i), end="")
    print("*"* (2*i-1))