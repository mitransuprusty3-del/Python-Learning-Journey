def Calculator(num_1 : float, ope : str, num_2 : float):
    if ope == "+":
        return num_1 + num_2
    elif ope == "-":
        return num_1 - num_2
    elif ope == "*":
        return num_1 * num_2
    elif ope == "/":
        if num_2 == 0:
            raise ZeroDivisionError
        return num_1 / num_2
    elif ope == "**":
        return num_1 ** num_2
    return None

try:
    num_1 : float = float(input("Enter num 1: "))
    ope : str = input("Enter operator: ").strip()
    num_2 : float = float(input("Enter num 2: "))

    print(f"{num_1} {ope} {num_2}")
except ValueError:
    print("Somthing went wront!")
except ZeroDivisionError:
    print("0 cannot be divided")
except Exception as e:
    print(f"Error: {e}")