city = input()
sales = float(input())
comission = 0
if city == "Sofia":
    if 0 <= sales and sales <= 500:
        comission = sales * 0.05
    elif 500 < sales and sales <= 1000:
        comission = sales * 0.07
    elif 1000 < sales and sales <= 10000:
        comission = sales * 0.08
    elif sales > 10000:
        comission = sales * 0.12
elif city == "Varna":
    if 0 <= sales and sales <= 500:
        comission = sales * 0.045
    elif 500 < sales and sales <= 1000:
        comission = sales * 0.075
    elif 1000 < sales and sales <= 10000:
        comission = sales * 0.1
    elif sales > 10000:
        comission = sales * 0.13
elif city == "Plovdiv":
    if 0 <= sales and sales <= 500:
        comission = sales * 0.055
    elif 500 < sales and sales <= 1000:
        comission = sales * 0.08
    elif 1000 < sales and sales <= 10000:
        comission = sales * 0.12
    elif sales > 10000:
        comission = sales * 0.145
if city in "Sofia Varna Plovdiv" and sales > 0:
    print(f"{comission:.2f}")
else:
    print("error")