rooms = [0] * int(input())
all_good = 0
free_chairs = 0
for i in range(1, len(rooms) + 1):
    data = input().split(" ")
    chair_diff = len(data[0]) - int(data[1])
    if chair_diff >= 0:
        all_good += 1
    else:
        print(f"{abs(chair_diff)} more chairs needed in room {i}")
    free_chairs += chair_diff
if all_good == len(rooms):
    print(f"Game On, {free_chairs} free chairs left")
