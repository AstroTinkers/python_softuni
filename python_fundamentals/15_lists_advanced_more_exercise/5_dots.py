def dots(starting, next_place):
    if next_place == ".":
        dots(starting, next_place)


rows = int(input())
start = []
board = [input().split(" ") for i in range(0, rows)]
for idxi, i in enumerate(board):
    for idxj, j in enumerate(i):
        if j == ".":
            start.append([idxi, idxj])


print()
