input_line = input().split(">>")
total_tax = 0
allowed = ["family", "heavyDuty", "sports"]
for i in input_line:
    i = i.split()
    if i[0] not in allowed:
        print("Invalid car type.")
    else:
        if i[0] == "family":
            tax = 50
            tax -= int(i[1]) * 5
            tax += (int(i[2]) // 3000) * 12
            total_tax += tax
            print(f"A {i[0]} car will pay {tax:.2f} euros in taxes.")
        elif i[0] == "heavyDuty":
            tax = 80
            tax -= int(i[1]) * 8
            tax += (int(i[2]) // 9000) * 14
            total_tax += tax
            print(f"A {i[0]} car will pay {tax:.2f} euros in taxes.")
        elif i[0] == "sports":
            tax = 100
            tax -= int(i[1]) * 9
            tax += (int(i[2]) // 2000) * 18
            total_tax += tax
            print(f"A {i[0]} car will pay {tax:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
