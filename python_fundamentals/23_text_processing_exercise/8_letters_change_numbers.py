def pos_in_alphabet(char):
    return char - 96


final_sum = 0
input_string = input().split()
for string in input_string:
    first_letter = string[0].lower()
    last_letter = string[-1].lower()
    num = int(string[1:-1])
    num_sum = 0
    if string[0].isupper():
        num_sum += num / pos_in_alphabet(ord(first_letter))
    else:
        num_sum += num * pos_in_alphabet(ord(first_letter))
    if string[-1].isupper():
        num_sum -= pos_in_alphabet(ord(last_letter))
    else:
        num_sum += pos_in_alphabet(ord(last_letter))
    final_sum += num_sum
print(f"{final_sum:.2f}")
