import re
phones = input()
matches = re.findall(r"(\+359(\s{1}|-)2\2\d{3}\2\d{4})\b", phones)
valid_phones = []
for i in matches:
    valid_phones.append(i[0])
print(", ".join(valid_phones))
