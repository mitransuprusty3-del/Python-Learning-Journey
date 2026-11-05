def swap(a, b):
    a, b = b, a
    print("After swapping:")
    print("a =", a)
    print("b =", b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

swap(x, y)