neighborhood = [int(i) for i in input().split("@")]
command = input()
position = 0
while command != "Love!":
    command = command.split()
    command, jump = command[0], int(command[1])
    position = position + jump if position + jump <= len(neighborhood) - 1 else 0
    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {position}.")
if sum(neighborhood) != 0:
    failed_places = [i for i in neighborhood if i != 0]
    print(f"Cupid has failed {len(failed_places)} places.")
else:
    print("Mission was successful.")

