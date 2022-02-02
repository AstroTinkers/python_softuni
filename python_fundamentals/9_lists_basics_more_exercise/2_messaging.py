numbers = input().split(" ")
text = list(input())
character = 0
message = []
for i in numbers:
    for j in i:
        character += int(j)
    while character > len(text):
        character -= len(text)
    else:
        message.append(text[character])
        text.pop(character)
    character = 0
print("".join(message))
