start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
combination_found = False
for i in range(start, end + 1):
    for x in range(start, end + 1):
        counter += 1
        if i + x == magic_number:
            print(f"Combination N:{counter} ({i} + {x} = {magic_number})")
            combination_found = True
            break
    if combination_found:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")
