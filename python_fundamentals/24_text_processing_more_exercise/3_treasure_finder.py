from math import ceil
import re
key = [int(el) for el in input().split()]
command = input()
while command != "find":
    key_extend = key * ceil(len(command) / len(key))
    decoded_command = "".join([chr(ord(command[char]) - key_extend[char]) for char in range(len(command))])
    treasure = "".join(re.findall(r"&(\w+)&", decoded_command))
    coordinates = "".join(re.findall(r"<(\w+)>", decoded_command))
    print(f"Found {treasure} at {coordinates}")
    command = input()
