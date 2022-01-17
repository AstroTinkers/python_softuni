iterations = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(iterations):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number and number <= 399:
        p2 += 1
    elif 400 <= number and number <= 599:
        p3 += 1
    elif 600 <= number and number <= 799:
        p4 += 1
    elif number >= 800:
        p5 += 1
p1_perc = (p1 / iterations) * 100
p2_perc = (p2 / iterations) * 100
p3_perc = (p3 / iterations) * 100
p4_perc = (p4 / iterations) * 100
p5_perc = (p5 / iterations) * 100
print(f"{p1_perc:.2f}%")
print(f"{p2_perc:.2f}%")
print(f"{p3_perc:.2f}%")
print(f"{p4_perc:.2f}%")
print(f"{p5_perc:.2f}%")