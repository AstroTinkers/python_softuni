def longer_string(str1, str2):
    return str1 if len(str1) >= len(str2) else str2


def shorter_string(str1, str2):
    return str1 if len(str1) < len(str2) else str2


input_string1, input_string2 = input().split()
char_sum = 0
long_str = longer_string(input_string1, input_string2)
short_str = shorter_string(input_string1, input_string2)
for char in range(len(short_str)):
    char_sum += ord(short_str[char]) * ord(long_str[char])
for char in range(len(long_str) - 1, len(short_str) - 1, -1):
    char_sum += ord(long_str[char])
print(char_sum)
