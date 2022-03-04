resource = input()
reserve = {}
while resource != "stop":
    quantity = int(input())
    reserve.setdefault(resource, 0)
    reserve[resource] += quantity
    resource = input()
for res, quan in reserve.items():
    print(f"{res} -> {quan}")
