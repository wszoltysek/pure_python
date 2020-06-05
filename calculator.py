print("## WELCOME TO CALCULATOR ##")
intro = """
OPTIONS:
1 - add
2 - subtract
3 - multiply
4 - divide
"""
print(intro)
choice = input("Type option number: ")

try:
    if choice == "1":
        x = int(input("First number: "))
        y = int(input("Second number: "))


        def add(x, y):
            """Add Function"""
            return x + y


        print(f"\nResult of add {x} + {y} is {add(x, y)}.")

    elif choice == "2":
        x = int(input("First number: "))
        y = int(input("Second number: "))


        def subtract(x, y):
            """Subtract Function"""
            return x - y


        print(f"\nResult of subtract {x} - {y} is {subtract(x, y)}.")

    elif choice == "3":
        x = int(input("First number: "))
        y = int(input("Second number: "))


        def multiply(x, y):
            """Multiply Function"""
            return x * y


        print(f"\nResult of multiply {x} * {y} is {multiply(x, y)}.")

    elif choice == "4":
        x = int(input("First number: "))
        y = int(input("Second number: "))


        def divide(x, y):
            """Divide Function"""
            if x == 0 or y == 0:
                raise ValueError("Can not divide by zero!")
            return x / y


        print(f"\nResult of divide {x} / {y} is {divide(x, y)}.")

    else:
        print("Invalid command. Try again.")

except ValueError:
    print("Wrong number. Must be int.")
