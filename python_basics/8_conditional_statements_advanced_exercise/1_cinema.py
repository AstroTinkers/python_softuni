screening = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns
if screening == "Premiere":
    income = capacity * 12
elif screening == "Normal":
    income = capacity * 7.5
elif screening == "Discount":
    income = capacity * 5
print(f"{income:.2f}")