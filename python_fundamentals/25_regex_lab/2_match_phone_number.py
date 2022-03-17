import re
phones = input()
matches = re.findall(r"(\+359(\s{1}|-)2\2\d{3}\2\d{4})\b", phones)
print(", ".join(matches))
