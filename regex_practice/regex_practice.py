import re

with open("data.txt", "r") as data:
    data_file = data.read()

# full name:
full_name_pattern = re.compile(r"[A-Z]{1}[a-z]{3,10}\s[A-Z]{1}[a-z]{3,10}")
fn_matches = full_name_pattern.finditer(data_file)

for match in fn_matches:
    print(match.group())
