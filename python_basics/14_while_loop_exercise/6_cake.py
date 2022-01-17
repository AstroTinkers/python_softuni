lenght = int(input())
width = int(input())
cake = lenght * width
cake_over = False
while cake_over != True:
    command = input()
    if command == "STOP":
        print(f"{cake} pieces are left.")
        break
    else:
        cake -= int(command)
        if cake < 0:
            cake_over = True
            break
if cake_over:
    print(f"No more cake left! You need {abs(cake)} pieces more.")