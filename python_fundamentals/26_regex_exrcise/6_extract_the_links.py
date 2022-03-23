import re
text = input()
links = []
pattern = r"www\.[a-zA-Z-\d]+\.[a-zA-Z]+\.?([\.a-zA-Z\d-]+)?"
while not text == "":
    links += [match.group() for match in re.finditer(pattern, text)]
    text = input()
print(*links, sep="\n")
