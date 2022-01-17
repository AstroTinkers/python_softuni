day_goal = int(input())
goal_complete = False
money = 0
while not goal_complete:
    order = input()
    if order == "closed":
        break
    elif order == "haircut":
        order2 = input()
        if order2 == "mens":
            money += 15
            if money >= day_goal:
                goal_complete = True
                break
        elif order2 == "ladies":
            money += 20
            if money >= day_goal:
                goal_complete = True
                break
        elif order2 == "kids":
            money += 10
            if money >= day_goal:
                goal_complete = True
                break
    elif order == "color":
        order3 = input()
        if order3 == "touch up":
            money += 20
            if money >= day_goal:
                goal_complete = True
                break
        elif order3 == "full color":
            money += 30
            if money >= day_goal:
                goal_complete = True
                break
difference = day_goal - money
if goal_complete:
    print("You have reached your target for the day!")
    print(f"Earned money: {money}lv.")
else:
    print(f"Target not reached! You need {difference}lv. more.")
    print(f"Earned money: {money}lv.")
