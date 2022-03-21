import re
input_text = input()
search_word = input().lower()
pattern = re.compile(search_word)
matches = re.findall(pattern, input_text.lower())
print(len(matches))
