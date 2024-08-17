'''Write a python function to print first n lines of the following pattern:
***
** 
*
'''
def func(n):
    if(n<=0):
        return 
    else:
        print("*"*n)
        return (func(n-1))
i=int(input("enter a number"))
func(i)