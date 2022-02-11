vowels = ['a', 'o', 'u', 'e', 'i']
phrase = [character for character in input()]
new_phrase = [i for i in phrase if i.lower() not in vowels]
new_phrase = "".join(new_phrase)
print(new_phrase)
