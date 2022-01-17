hour = int(input())
minute = int(input())
minute += 15

hour += minute // 60
minute %= 60

if hour == 24:
    hour = 0

print(f"{hour}:{minute:02d}")
