steps = input()
actual_steps = 0
steps_count = 0
difference = 0
while steps != "Going home":
    actual_steps = float(steps)
    steps_count += actual_steps
    if steps_count >= 10000:
        difference = int(abs(steps_count - 10000))
        print("Goal reached! Good job!")
        print(f"{difference} steps over the goal!")
        break
    steps = input()
else:
    steps = int(input())
    steps_count += steps
    difference = int(abs(steps_count - 10000))
    if steps_count >= 10000:
        print("Goal reached! Good job!")
        print(f"{difference} steps over the goal!")
    else:
        print(f"{difference} more steps to reach goal.")