name = input("enter your name: ")
phy=int(input("enter your physics mark: "))
che=int(input("enter your chemistary mark: "))
math=int(input("enter your math mark: "))
biologyorit=int(input("enter your biology or IT mark: "))
odia=int(input("enter your odia mark: "))
english=int(input("enter your english mark: "))

if phy > 100 or phy < 0:
    print("invalid mark")
elif che > 100 or che < 0:
    print("invalid mark")
elif math > 100 or math < 0:
    print("invalid mark")
elif biologyorit > 100 or biologyorit  < 0:
    print("invalid mark")
elif odia > 100 or odia < 0:
    print("invalid mark")
elif english > 100 or english < 0:
    print("invalid mark")
else:


    total_mark = phy + che + math + biologyorit + odia + english


    percentage = (total_mark/600)*100

    print("--"*6,"student result","--"*6)
    print("your name is: ",name)
    print("total mark is equal to: ",total_mark)
    print("percentage is equal to: ",percentage)

    if percentage>=30 and percentage<50:
        print(" grade b")
    elif percentage >=50 and percentage<70:
        print("grade b+")
    elif percentage>=70 and percentage<90:
        print("a")
    elif percentage>=90 and percentage<100:
        print("a+")
    else :

        print("tou are fail")    
