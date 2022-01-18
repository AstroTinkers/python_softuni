phrase = input()
phrase_upper = []
for i in range(len(phrase)):
    if phrase[i].isupper():
        phrase_upper.append(i)
print(phrase_upper)