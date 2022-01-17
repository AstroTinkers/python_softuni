from math import ceil
name_series = str(input())
episode_length = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
recreation_time = break_duration / 4

total_time = episode_length + lunch_time + recreation_time
difference = break_duration - total_time
if break_duration >= total_time:
    print(f"You have enough time to watch {name_series} and left with {ceil(abs(difference))} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {ceil(abs(difference))} more minutes.")