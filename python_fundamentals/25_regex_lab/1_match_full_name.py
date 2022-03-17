import re
names = input()
matches = re.findall(r"\b[A-Z]{1}[a-z]{1,} [A-Z]{1}[a-z]{1,}\b", names)
print(" ".join(matches))
