print("## WELCOME TO CALCULATOR ##")
intro = """
Insert calculator choice:
1 - add
2 - subtract
3 - multiply
4 - divide
"""
print(intro)
choice = input("Your choice: ")
x = int(input("First number: "))
y = int(input("Second number: "))

if choice == "1":

    def add(x, y):
        """Add Function"""
        return x + y

    print(f"\nResult of add {x} + {y} is {add(x, y)}.")

elif choice == "2":

    def subtract(x, y):
        """Subtract Function"""
        return x - y

    print(f"\nResult of subtract {x} - {y} is {subtract(x, y)}.")

elif choice == "3":

    def multiply(x, y):
        """Multiply Function"""
        return x * y

    print(f"\nResult of multiply {x} * {y} is {multiply(x, y)}.")

elif choice == "4":

    def divide(x, y):
        """Divide Function"""
        if x == 0 or y == 0:
            raise ValueError("Can not divide by zero!")
        return x / y

    print(f"\nResult of divide {x} / {y} is {divide(x, y)}.")

else:
    print("Invalid command. Try again.")
