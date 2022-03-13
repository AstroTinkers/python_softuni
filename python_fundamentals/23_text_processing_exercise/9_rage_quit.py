import re

input_message = input()
unique_chars = set(el.upper() for el in input_message if not el.isnumeric())
char_strings = [char.upper() for char in re.findall(r"\D+", input_message)]
num_strings = [int(num) for num in re.findall(r"\d+", input_message)]
rage_quit_message = ""

for chars in range(len(char_strings)):
    rage_quit_message += char_strings[chars] * num_strings[chars]

print(f"Unique symbols used: {len(unique_chars)}")
print(rage_quit_message)
