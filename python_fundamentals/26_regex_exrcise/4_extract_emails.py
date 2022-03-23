import re
input_data = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
emails_found = [email.group() for email in re.finditer(pattern, input_data)]
print(*emails_found, sep="\n")
