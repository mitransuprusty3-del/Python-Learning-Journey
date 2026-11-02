
balance = 5000
while True:
    print("\n======== welcome to our atm =========")
    print("1.check bank blance ")
    print("2.deposite amount ")
    print("3.widrow amount ")
    print("4.exit or clear")

    choose = input("choose a number according to you :")

    if choose == "1":
        print(" your balance is: ",balance)
    elif choose == "2":
        amount = int(input("enter your amount: "))
        if amount<0 :
            print("invalid amount")
        else:
            total_balance = balance = balance + amount
            print("deposit sucessful")
            print("total balance is equal to : ",total_balance)

            

    elif choose =="3":
        amount = int(input("enter your widral amount"))
        if amount<5000 and amount<0:
            print("not valid")
        else:
            total_balance = balance = balance - amount
            print("widral sucessfully")
            print("total  balance is equal to",total_balance)
    elif choose == "4":
        print("thank you for using our atm")
        break
    else:
        print("invalid option")