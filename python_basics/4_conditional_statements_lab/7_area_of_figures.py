from math import pi
figure = str(input())
if figure == "square":
    side_a = float(input())
    area_sq = side_a * side_a
    print(f"{area_sq:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    rad = float(input())
    area = rad * rad * pi
    print(f"{area:.3f}")
elif figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a * side_b) / 2
    print(f"{area:.3f}")