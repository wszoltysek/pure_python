import sys

print("## WELCOME TO CALCULATOR ##")

finish = False
while not finish:

    intro = """
    SELECT OPTIONS:
    1 - add
    2 - subtract
    3 - multiply
    4 - divide
    """
    print(intro)
    choice = input("Type option number: ")
    while choice not in ["1", "2", "3", "4"]:
        print("Choice incorrect. Try again.")
        choice = input("Type option number: ")

    try:
        if choice == "1":
            print("# Addition #\n")
            x = float(input("First number: "))
            y = float(input("Second number: "))


            def add(x, y):
                """Add Function"""
                return x + y


            print(f"\nResult of add {x} + {y} is {add(x, y)}.")

        elif choice == "2":
            print("Subtraction\n")
            x = float(input("First number: "))
            y = float(input("Second number: "))


            def subtract(x, y):
                """Subtract Function"""
                return x - y


            print(f"\nResult of subtract {x} - {y} is {subtract(x, y)}.")

        elif choice == "3":
            print("Multiplication\n")
            x = float(input("First number: "))
            y = float(input("Second number: "))


            def multiply(x, y):
                """Multiply Function"""
                return x * y


            print(f"\nResult of multiply {x} * {y} is {multiply(x, y)}.")

        elif choice == "4":
            print("Division\n")
            x = float(input("First number: "))
            y = float(input("Second number: "))


            def divide(x, y):
                """Divide Function"""
                if x == 0 or y == 0:
                    raise ValueError("Can not divide by zero!")
                return x / y


            print(f"\nResult of divide {x} / {y} is {divide(x, y)}.")

    except ValueError:
        print("Incorrect value. Must be int or float.")

    if "yes" == input("\nDo you want to start over? [Write \"yes\" or type any key to exit.] \n"):
        print("Thanks for using calculator again!")
    else:
        done = True
        print("Thanks for using calculator. GoodBye!")
        sys.exit()
