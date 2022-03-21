import re
input_data = input()
pattern = r"([a-zA-Z0-9]{1,}[\-\.\_a-zA-Z0-9]{1,})@([a-zA-Z0-9]{1,}[\-\.\_a-zA-Z0-9]*)"
emails_found = re.findall(pattern, input_data)
for email in emails_found:
    print(email)
