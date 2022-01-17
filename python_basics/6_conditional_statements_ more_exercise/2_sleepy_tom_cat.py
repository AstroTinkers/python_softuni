holidays = int(input())

playtime = ((365 - holidays) * 63) + (holidays * 127)
difference = abs(30000 - playtime)
hours = difference // 60
minutes = difference % 60
if playtime > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")