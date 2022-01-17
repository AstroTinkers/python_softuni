n_computers = int(input())
sales = 0
rating = 0
for n in range(1, n_computers + 1):
    sales_rating = int(input())
    if sales_rating % 10 == 2:
        rating += 2
    elif sales_rating % 10 == 3:
        rating += 3
        sales += int(sales_rating / 10) * 0.5
    elif sales_rating % 10 == 4:
        rating += 4
        sales += int(sales_rating / 10) * 0.7
    elif sales_rating % 10 == 5:
        rating += 5
        sales += int(sales_rating / 10) * 0.85
    elif sales_rating % 10 == 6:
        rating += 6
        sales += int(sales_rating / 10)
average = rating / n_computers
print(f"{sales:.2f}")
print(f"{average:.2f}")
