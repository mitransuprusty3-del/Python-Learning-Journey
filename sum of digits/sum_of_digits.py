a=int(input("enter your number: "))
total = 0

while a > 0 :
    digit = a % 10
    total = total + digit
    a = a//10

print("sum:",total)    