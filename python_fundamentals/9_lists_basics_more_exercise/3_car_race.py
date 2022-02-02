race_track = input().split(" ")
left_car_time = 0
right_car_time = 0
for i in race_track[:len(race_track) // 2]:
    if int(i) == 0:
        left_car_time = left_car_time * 0.8
    else:
        left_car_time += int(i)
for j in race_track[:len(race_track) // 2: -1]:
    if int(j) == 0:
        right_car_time = right_car_time * 0.8
    else:
        right_car_time += int(j)
winner = "left" if left_car_time < right_car_time else "right"
win_time = left_car_time if winner == "left" else right_car_time
print(f"The winner is {winner} with total time: {win_time:.1f}")
