input_string = input()
digits = ""
letters = ""
other = ""
for i in input_string:
    if i.isnumeric():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        other += i
print(digits)
print(letters)
print(other)
