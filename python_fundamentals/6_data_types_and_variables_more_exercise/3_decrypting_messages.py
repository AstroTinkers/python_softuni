key = int(input())
lines = int(input())
message = []
for i in range(lines):
    letter = input()
    message.append(chr(ord(letter) + key))
message_decrypted = ''.join(message)
print(message_decrypted)
