usernames = input().split(", ")
valid_usernames = []
allowed_chars = [i for i in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"]
for user in usernames:
    if 3 > len(user) > 16:
        continue
    if all(char in allowed_chars for char in user):
        print(user)
