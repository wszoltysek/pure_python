import argparse
import sys

done = False
while not done:

    class FileAnalizer:

        def __init__(self, filename):
            self.filename = filename
            self.all_char_counter = 0
            self.sentence_counter = 0
            self.upper_counter = 0
            self.lower_counter = 0
            self.dots_counter = 0
            self.comas_counter = 0
            self.digits_counter = 0
            self.spaces_counter = 0
            self.special_counter = 0
            self.special_list = ["!", "?", "@", "#", "$", "%", "^", "&", "*", "-", "+", "=", "_", ":", ";"]
            self.other_counter = 0

        def process_file(self):
            with open(self.filename, "r") as input_file:
                txt_file = input_file.read()
                self.all_char_counter = len(txt_file)
                self.sentence_counter = len(txt_file.split(". "))

                for char in txt_file:
                    if char.isupper():
                        self.upper_counter += 1
                    elif char.islower():
                        self.lower_counter += 1
                    elif char == ".":
                        self.dots_counter += 1
                    elif char == ",":
                        self.comas_counter += 1
                    elif char.isnumeric():
                        self.digits_counter += 1
                    elif char.isspace():
                        self.spaces_counter += 1
                    elif char in self.special_list:
                        self.special_counter += 1
                    else:
                        self.other_counter += 1


    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, action="store")

    if len(sys.argv) < 2:
        print()
        print("WELCOME TO TEXT FILE ANALIZER")
        print("This program analyzes the data from users txt file.")
        print("To run a program write: \"python3 file_analizer.py your_txt_file.txt\" ")
        print()
        sys.exit()

    else:
        options = parser.parse_args()
        file = FileAnalizer(options.filename)
        file.process_file()

        if file.all_char_counter == 0:
            print()
            print("Your text file is empty.")
            print()
        else:
            print(f"Your text file have {file.all_char_counter} characters.")
            print()
            print("There are:")
            print(f"{file.sentence_counter} sentences,")
            print(f"{file.upper_counter} upper letters,")
            print(f"{file.lower_counter} lower letters,")
            print(f"{file.dots_counter} dots,")
            print(f"{file.comas_counter} comas,")
            print(f"{file.spaces_counter} white spaces,")
            print(f"{file.digits_counter} digits,")
            print(f"{file.special_counter} special characters like: !, ?, #, %, * etc,")
            print(f"and {file.other_counter} other characters.")
            print()

    if "yes" == input("Do you want to start over? [Write \"yes\" or \"no\"] "):
        print()
        print("WELCOME AGAIN!")
        print("To run a program write: \"python3 file_analizer.py <your_txt_file_name>.txt\" ")
        print()
        sys.exit()
    else:
        done = True
        sys.exit()
