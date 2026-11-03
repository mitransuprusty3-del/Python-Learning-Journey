print("======welcome to laxminarayan bastralaya======")



dress1=input("enter your 1st product: ")
dress2=input("enter your 2nd product: ")

qt1=int(input("enter your 1st product quantity: "))
qt2=int(input("enter your 2nd product quantity: "))

pt1=int(input("enter your 1st product price: "))
pt2=int(input("enter your 2nd product price:  "))

amount=(qt1*pt1)+(qt2*pt2)
print("\n")
print("========bill==========")

tax=amount*0.05
print(f"1.{pt1} x {qt1} = {pt1*qt1}")
print(f"2.{pt2} x {qt2} = {pt2*qt2}")
print(f"gst 5%            {tax}")
print("--"*20)
print(f"total             {amount}")
print("tank you visit agaain!")





