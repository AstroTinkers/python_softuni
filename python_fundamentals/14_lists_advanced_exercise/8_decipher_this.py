message = input().split()
secret_message = []
for i in message:
    text = [chr(int("".join(j for j in i if j.isnumeric())))] + [m for m in i if not m.isnumeric()]
    text[1], text[-1] = text[-1], text[1]
    secret_message.append("".join(text))
secret_message = " ".join(secret_message)
print(secret_message)
