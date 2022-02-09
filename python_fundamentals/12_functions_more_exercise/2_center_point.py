from math import sqrt, floor


def distance_to_zero(horizontal, vertical):
    return sqrt((horizontal - 0) ** 2 + (vertical - 0) ** 2)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
if distance_to_zero(x_1, y_1) > distance_to_zero(x_2, y_2):
    print(f"({int(floor(x_2))}, {int(floor(y_2))})")
else:
    print(f"({int(floor(x_1))}, {int(floor(y_1))})")
