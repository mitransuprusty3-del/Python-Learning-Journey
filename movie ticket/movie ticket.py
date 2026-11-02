print("=======welcome to mitra multiplex=========")
print("a.toxic")
print("b.sayara")
print("c.jailor")
print("d.animal")
name = input("enter your name: ")
choose = input("enter your choice of movie: ")

if choose == "a":
    print("movie = toxic")
elif choose == "b":
    print("sayara")
elif choose == "c":
    print("jailor")
elif choose == "d":
    print("animal")
else:
    print("invalid choice")
exit()

print("\nmovie time table: ")
print("1.   10 am")
print("2.   12.30 am")
print("3.   2pm")
print("4.   10pm")

choose = input("enter your choice")

if choose=="1":
    print("10 am")
elif choose=="2":
    print("12.30am")

elif choose=="3":
    print("2 pm")

elif choose=="4":
    print("10 pm")
else:
    print("invalid choice")
exit()

ticket = int(input("enter number of ticket: "))
ticket = 200

if ticket<=0:
    total = ticket * 200

print("=====total information=====")
print("enter your name: ",name)
print("")







