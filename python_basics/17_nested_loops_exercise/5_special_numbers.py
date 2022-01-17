number = int(input())
magic_counter = 0
is_special = False
for i in range(1111, 9999 + 1):

    for index, value in enumerate(str(i)):

        if value == "0":
            break
        elif number % int(value) == 0:
            magic_counter += 1

        if magic_counter == 4:
            is_special = True

    if is_special:
        print(i, end=" ")

    magic_counter = 0
    is_special = False
