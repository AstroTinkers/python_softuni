def characters(beginning, end):
    return [chr(i) for i in range(ord(beginning) + 1, ord(end))]


character_1, character_2 = input(), input()
print(" ".join(characters(character_1, character_2)))
