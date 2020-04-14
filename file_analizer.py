done = False
while not done:

    print()
    print("WELCOME!")
    print("This program analyzes the data entered by the user")
    print()
    pony = input("Enter your data: ")

    dots_count = pony.count(".")
    coma_count = pony.count(",")
    sentence_count = len(pony.split(". "))


    def upper_letters_counter(pony):
        upperletters = 0
        for letter in pony:
            if letter.isupper():
                upperletters += 1
        return upperletters


    def lower_letters_counter(pony):
        lowerletters = 0
        for letter in pony:
            if letter.islower():
                lowerletters += 1
        return lowerletters


    def numbers_counter(pony):
        digits = 0
        for mark in pony:
            if mark.isdigit():
                digits += 1
        return digits


    def special_counter(pony):
        special_list = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "=", "_"]
        counter = 0
        for special in pony:
            if special in special_list:
                counter += 1
        return counter


    if len(pony) == 0:
        print()
        print("Wiersz nie może być pusty.")
        print()
    else:
        print()
        print(f"Długość wiersza to {len(pony)} znaków.")
        print(f"Wiersz ma {sentence_count} zdania.")
        print(f"Wiersz ma {upper_letters_counter(pony)} dużych liter.")
        print(f"Wiersz ma {lower_letters_counter(pony)} małych liter.")
        print(f"Wiersz ma {dots_count} kropki.")
        print(f"Wiersz ma {coma_count} przecinków.")
        print(f"Wiersz ma {numbers_counter(pony)} liczb.")
        print(f"Wiersz ma {special_counter(pony)} znaków specjalnych.")
        print()

    if "yes" != input("Do you want to start over? [Write \"yes\" or \"no\"] "):
        done = True

    # TODO: If-owanie printami w zależności od ilości.
    # TODO: Wszystko po angielsku
