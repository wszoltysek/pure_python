import sys
from apps_messages.analyzer_msgs import *

print(start_msg)
done = False
while not done:

    class FileAnalyzer:
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
            self.character = ""

        def process_file(self):
            with open(self.filename, "r") as input_file:
                txt_file = input_file.read()
                self.all_char_counter = len(txt_file)
                self.sentence_counter = len(txt_file.split(". "))

                for char in txt_file:
                    self.character = char
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

    user_file = input("Enter your txt file for analysis: ")
    try:
        file = FileAnalyzer(user_file)
        file.process_file()

        if file.all_char_counter == 0:
            print("\nYour text file is empty.\n")
        else:
            if file.all_char_counter == 1:
                print(f"\nYour text file have {file.all_char_counter} character.")
                print(f"It's {file.character}.\n")
            else:
                print(f"\nYour text file have {file.all_char_counter} characters.\n")
                print("There are:\n")
                print(f"{file.sentence_counter} sentences,")
                print(f"{file.upper_counter} upper letters,")
                print(f"{file.lower_counter} lower letters,")
                print(f"{file.dots_counter} dots,")
                print(f"{file.comas_counter} comas,")
                print(f"{file.spaces_counter} white spaces,")
                print(f"{file.digits_counter} digits,")
                print(f"{file.special_counter} special characters like: !, ?, #, %, * etc,")
                print(f"and {file.other_counter} other characters.\n")

    except FileNotFoundError:
        print(file_error)

    if "yes" == input("Do you want to start over with a different file?\n"
                      "[Write \"yes\" or type any key to exit.] \n"):
        print(repeat_msg)
    else:
        done = True
        print(end_msg)
        sys.exit()
