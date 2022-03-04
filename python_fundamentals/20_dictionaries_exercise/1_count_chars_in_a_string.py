text = [x for x in input() if x != " "]
char_dict = {char: 0 for char in text}
for i in text:
    char_dict.setdefault(i, 0)
    char_dict[i] += 1
for key, value in char_dict.items():
    print(f"{key} -> {value}")
