a=int(input("enter your first number: "))
b=int(input ("enter your second number: "))
c=int(input("enter your third number: "))
if a>=b and a>=c:
    print("greatest number is:",a)
elif b>=a and b>=c:
    print("greatest number is:",b)
else:
    print("greatest number is:",c)