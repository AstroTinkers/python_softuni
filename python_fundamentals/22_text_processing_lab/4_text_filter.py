ban_words = input().split(", ")
text_string = input()
for word in ban_words:
    if word in text_string:
        text_string = text_string.replace(word, "*" * len(word))
print(text_string)
