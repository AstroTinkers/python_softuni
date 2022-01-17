number = int(input())
counter = 1
is_current_bigger = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if counter > number:
            is_current_bigger = True
            break
        else:
            print(counter, end=" ")
            counter += 1
    if is_current_bigger:
        break
    print()