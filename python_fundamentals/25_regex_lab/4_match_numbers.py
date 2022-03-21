import re
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = input()
matches = re.finditer(pattern, numbers)
for i in matches:
    print(i.group(), end=" ")
