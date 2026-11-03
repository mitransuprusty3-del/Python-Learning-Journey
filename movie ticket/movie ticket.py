print("===== MOVIE TICKET BOOKING =====")

name = input("Enter your name: ")

print("\n1. Normal Movie - Rs. 150")
print("2. 3D Movie - Rs. 250")
print("3. VIP Movie - Rs. 400")

choice = int(input("\nEnter your choice (1-3): "))

tickets = int(input("Enter number of tickets: "))

if choice == 1:
    price = 150
    movie_type = "Normal Movie"

elif choice == 2:
    price = 250
    movie_type = "3D Movie"

elif choice == 3:
    price = 400
    movie_type = "VIP Movie"

else:
    price = 0
    movie_type = "Invalid Choice"

if price > 0 and tickets > 0:
    total = price * tickets

    print("\n===== BOOKING DETAILS =====")
    print("Name:", name)
    print("Movie Type:", movie_type)
    print("Tickets:", tickets)
    print("Total Amount: Rs.", total)

else:
    print("Invalid choice or ticket quantity!")

print("\nThank You!")
