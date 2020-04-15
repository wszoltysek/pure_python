import argparse
import sys

class FileAnalizer:

    def __init__(self, filename):
        self.filename = filename
        self.file_counter = 0
        self.upper_counter = 0
        self.lower_counter = 0
        self.dots_counter = 0
        self.comas_counter = 0
        self.digits_counter = 0
        self.special_list = ["!", "?", "@", "#", "$", "%", "^", "&", "*", "-", "+", "=", "_", ":", ";"]
        self.special_counter = 0
        self.sentence_counter = 0

    def process_file(self):
        with open(self.filename, "r") as input_file:

            while True:
                char = input_file.read(1)
                self.file_counter += len(char)

                if not char:
                    break
                elif char.isupper():
                    self.upper_counter += 1
                elif char.islower():
                    self.lower_counter += 1
                elif char == ".":
                    self.dots_counter += 1
                elif char == ",":
                    self.comas_counter += 1
                elif char in self.special_list:
                    self.special_counter += 1
                elif char == ". ":
                    self.sentence_counter += 1


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

    if file.file_counter == 0:
        print()
        print("Your text file is empty.")
        print()
    else:
        print(f"Your text file have {file.file_counter} characters.")
        print()
        print("There are:")
        print(f"{file.upper_counter} upper letters,")
        print(f"{file.lower_counter} lower letters,")
        print(f"{file.dots_counter} dots,")
        print(f"{file.comas_counter} comas,")
        print(f"{file.special_counter} special characters like: !, ?, #, %, * etc.")
        # print("zdania", file.sentence_counter)
