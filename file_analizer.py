import argparse
import sys
from apps_messages.analizer_v1_msgs import start_msg, repeat_msg, end_msg

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


    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, action="store")

    if len(sys.argv) < 2:
        print(start_msg)
        sys.exit()

    else:
        try:
            options = parser.parse_args()
            file = FileAnalizer(options.filename)
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
            print("\nFile not found or invalid. \nStart over and enter the correct *.txt file.\n")
            sys.exit()

    if "yes" == input("Do you want to start over with a different file? "
                      "[Write \"yes\" or \"no\"] \n"):
        print(repeat_msg)
        sys.exit()
    else:
        done = True
        print(end_msg)
        sys.exit()
