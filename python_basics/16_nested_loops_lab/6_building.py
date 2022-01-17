floors = int(input())
rooms = int(input())
for i in range(floors, 0, -1):
    for x in range(rooms):
        if i == floors:
            print(f"L{i}{x}", end=" ")
        elif i % 2 == 0:
            print(f"O{i}{x}", end=" ")
        else:
            print(f"A{i}{x}", end=" ")
    print()
