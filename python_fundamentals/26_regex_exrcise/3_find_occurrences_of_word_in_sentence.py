import re
word_filter = r"\b[\S]+\b"
input_text = input()
matched_input = re.findall(word_filter, input_text)
search_word = input().lower()
found = [word for word in matched_input if word.lower() == search_word]
print(len(found))
