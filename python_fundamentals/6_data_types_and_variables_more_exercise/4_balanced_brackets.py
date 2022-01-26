lines = int(input())
left_bracket = 0
right_bracket = 0
is_nested = ""
nested = True
for i in range(lines):
    symbol = input()
    if symbol == is_nested:
        nested = False
        print("UNBALANCED")
        break
    elif symbol == "(":
        left_bracket += 1
    elif symbol == ")":
        right_bracket += 1
    is_nested = symbol
if nested:
    if left_bracket == right_bracket:
        print("BALANCED")
    else:
        print("UNBALANCED")
