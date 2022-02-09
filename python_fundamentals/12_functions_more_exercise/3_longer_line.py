from math import sqrt, floor


def distance(h_1, v_1, h_2, v_2):
    return sqrt((h_2 - h_1) ** 2 + (v_2 - v_1) ** 2)


def closer_to_zero(p_1, p_2):
    return p_1 > p_2


x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4 = float(input()), float(input()), float(input()), float(input()), \
                                         float(input()), float(input()), float(input()), float(input())


if distance(x_1, y_1, x_2, y_2) >= distance(x_3, y_3, x_4, y_4):
    if closer_to_zero(distance(x_1, y_1, 0, 0), distance(x_2, y_2, 0, 0)):
        print(f"({int(floor(x_2))}, {int(floor(y_2))})({int(floor(x_1))}, {int(floor(y_1))})")
    else:
        print(f"({int(floor(x_1))}, {int(floor(y_1))})({int(floor(x_2))}, {int(floor(y_2))})")
else:
    if closer_to_zero(distance(x_3, y_3, 0, 0), distance(x_4, y_4, 0, 0)):
        print(f"({int(floor(x_4))}, {int(floor(y_4))})({int(floor(x_3))}, {int(floor(y_3))})")
    else:
        print(f"({int(floor(x_3))}, {int(floor(y_3))})({int(floor(x_4))}, {int(floor(y_4))})")
