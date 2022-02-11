employ_happiness = map(int, input().split(" "))
happiness_improv_factor = int(input())
employ_happiness = list(map(lambda i: i * happiness_improv_factor, employ_happiness))
average_happiness = list(filter(lambda i: i >= sum(employ_happiness) / len(employ_happiness), employ_happiness))
if len(average_happiness) >= len(employ_happiness) / 2:
    print(f"Score: {len(average_happiness)}/{len(employ_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(average_happiness)}/{len(employ_happiness)}. Employees are not happy!")
