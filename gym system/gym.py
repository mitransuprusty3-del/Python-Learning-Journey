print("--------WELCOME TO MITRA GYM--------")
print("membership per month according to catagory")
print("1.basic")
print("2.standard")
print("3.premium")
print("4.vip")
print("5.visit")
name = input("enter your name: ")
mobille_number = int(input("enter your mobile number: "))
while true:
    if mobille_number>999999999 and mobille_number<10000000000:
        print("valid number")
        break
    else:
        print("not valid")
   

choose = input("enter your number for membership: ")

if choose == "1":
    print("price = 900")
    price = int(input("enter the price money: "))
    if price == 900:
        print("sucessfully purchise")
        print("you can do excercise")
    else:
        if price>900:
         print("take rest amount",price - 900)
        else:
            print("give rest amount",900-price)

elif choose == "2":
    print("price = 1300")
    price = int(input("enter the price money: "))
    if price == 1300:
        print("sucessfully purchise")
        print("you can do excercise")
    else:
        if price>1300:
            print("take rest amount",price-1300)
        else:
            print("give rest amount",1300-price)

elif choose == "3":
    print("price = 2000")
    price = int(input("enter the price money: "))
    if price == 2000:
        print("sucessfully purchise")
        print("you can do excercise")
    else:
        if price>2000:
            print("take rest amount",price-2000)
        else:
            print("give rest amount",2000-price)
        

elif choose == "4":
    print("price = 3000")
    price = int(input("enter the price money: "))
    if price == 3000:
        print("sucessfully purchise")
        print("you can do excercise")
    else:
        if price>3000:
            print("take rest amount",price-3000)
        else:
            print("give rest amount",3000-price)

elif choose == "5":
    print("a.creatine")
    print("b.protin")
    print("c.oats")
    print("d.only visit")
    choice = input("enter your choice: ")
    if choice == "a":
        print("price = 1000")
        price = int(input("enter your price: "))
        if price == 1000:
            print("sucessfully purchise")
        
        else:
            if price>1000:
                print("take rest amount",price - 1000)
            else:
                print("give rest amount",1000-price)

    elif choice == "b":
        print("price = 5000")
        price = int(input("enter your price: "))
        if price == 5000:
            print("sucessfully purchise")
        
        else:
            if price>5000:
                print("take rest amount",price - 5000)
            else:
                print("give rest amount",5000-price)    
    elif choice == "c":
        print("price = 2000")
        price = int(input("enter your price: "))
        if price == 2000:
            print("sucessfully purchise")
        
        else:
            if price>2000:
                print("take rest amount",price - 2000)
            else:
                print("give rest amount",2000-price)
    elif choice == "d":
        print("thank you for visiting")
    else:
        print(" invalid choice")
else:
    print("invalid choice")

