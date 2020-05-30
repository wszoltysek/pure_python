import re

with open("data.txt", "r") as data:
    data_file = data.read()

# full name:
full_name_pattern = re.compile(r"[A-Z]{1}[a-z]{3,10}\s[A-Z]{1}[a-z]{3,10}")
fn_matches = full_name_pattern.finditer(data_file)

# for match in fn_matches:
#     print(match.group())

# phone number:
phone_pattern = re.compile(r"\d{3}[*-.]+\d{3}[*-.]+\d{4}")
ph_matches = phone_pattern.finditer(data_file)

# for match in ph_matches:
#     print(match.group())

# adresses:
addr_pattern = re.compile(
    r"(\d{3}\s)([A-Za-z]+\s[A-Z]{1}[a-z]{1}[.|,]+\s)([A-Za-z]+\s)([A-Z]{2}\s)(\d+)"
)
addr_matches = addr_pattern.finditer(data_file)

# for match in addr_matches:
#     print(match.group())

# emails:
email_pattern = re.compile(r"([a-z]+)([.]*)([a-z]*)@([a-z]+)([\.a-z]+)([\.a-z]*)")
email_matches = email_pattern.finditer(data_file)

emails_list = [match.group() for match in email_matches]
print(emails_list)
