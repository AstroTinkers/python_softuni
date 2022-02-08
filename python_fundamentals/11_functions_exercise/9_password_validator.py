def is_long_enough(password):
    return 6 <= len(password) <= 10


def has_numbers(password):
    num_list = [x for x in password if x.isnumeric()]
    return len(num_list) >= 2


def allowed_chars(password):
    allowed_symbols = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return all([i in allowed_symbols for i in password])


def valid_password(password):
    return is_long_enough(password) and has_numbers(password) and allowed_chars(password)


password_input = input()
if valid_password(password_input):
    print("Password is valid")
else:
    if not is_long_enough(password_input):
        print("Password must be between 6 and 10 characters")
    if not allowed_chars(password_input):
        print("Password must consist only of letters and digits")
    if not has_numbers(password_input):
        print("Password must have at least 2 digits")
