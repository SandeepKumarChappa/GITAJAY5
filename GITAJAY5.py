##PYTHON CODE TO PRINT FACTORIAL OF NUMBERS
def factnum(n):
    mul=1
    for i in range(1,n+1):
        mul=mul*i
    print(mul)
a=int(input("enter a number"))
factnum(a)

