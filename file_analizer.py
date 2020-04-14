done = False
while not done:

    print("WELCOME!")
    print("This program analyzes the data entered by the user")
    pony = input("Enter your data: ")

    dots_count = pony.count(".")
    coma_count = pony.count(",")
    sentence_count = len(pony.split(". "))


    def count_upper_letters(pony):
        upperletters = 0
        for letter in pony:
            if letter.isupper():
                upperletters += 1
        return upperletters


    def count_lower_letters(pony):
        lowerletters = 0
        for letter in pony:
            if letter.islower():
                lowerletters += 1
        return lowerletters


    def special_counter(pony):
        special_list = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "=", "_"]
        counter = 0
        for special in pony:
            if special in special_list:
                counter += 1
        return counter


    if len(pony) == 0:
        print("Wiersz nie moze byc pusty")
    else:
        print()
        print("Długość wiersza to", len(pony), "znaków.")
        print("Wiersz ma", count_upper_letters(pony), "dużych liter.")
        print("Wiersz ma", count_lower_letters(pony), "małych liter.")
        print("Wiersz ma", dots_count, "kropki.")
        print("Wiersz ma", coma_count, "przecinków.")
        print("Wiersz ma", sentence_count, "zdania.")
        print("Wiersz ma", special_counter(pony), "znaków specjalnych.")

    if 'yes' != input("Do you want to start over? "):
        done = True
    # input("Press enter to exit")

    # TODO: If-owanie printami w zależności od ilości.
