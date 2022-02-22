rows = int(input())
ships = [list(map(int, input().split())) for i in range(0, rows)]
destroyed = 0
attack = input().split(" ")
for i in attack:
    row, column = i.split("-")
    row, column = int(row), int(column)
    if ships[row][column] != 0:
        ships[row][column] -= 1
        if ships[row][column] == 0:
            destroyed += 1
print(destroyed)
