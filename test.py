import argparse
import sys


class FileAnalizer:

    def __init__(self, filename):
        self.filename = filename
        self.counter = 0
        self.dots_counter = 0

    def process_file(self):
        with open(self.filename, "r") as input_file:
            while True:
                char = input_file.read(1)
                if not char:
                    break

                if char.isupper():
                    self.counter += 1
                elif char == ".":
                    self.dots_counter += 1


parser = argparse.ArgumentParser()
parser.add_argument("command", type=str, action="store")
options = parser.parse_args()
command = options.command

if command is None:
    print()
    print("WELCOME!")
    print("This program analyzes the data entered by the user")
    print()
    sys.exit(0)

elif command == "filename":
    file = FileAnalizer(options.filename)
    file.process_file()

    print(file.counter)
    print(file.dots_counter)
