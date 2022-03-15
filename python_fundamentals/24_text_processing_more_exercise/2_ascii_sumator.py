start, stop, string_to_sum = ord(input()), ord(input()), input()
chars_sum = [ord(char) for char in string_to_sum if start < ord(char) < stop]
print(sum(chars_sum))
