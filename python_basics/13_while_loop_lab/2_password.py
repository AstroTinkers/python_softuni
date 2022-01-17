user = input()
password = input()
pass_in = input()
while password != pass_in:
    pass_in = input()
else:
    print(f"Welcome {user}!")