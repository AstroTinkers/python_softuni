groups = int(input())
Musala = 0
Montblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0
people_total = 0
for i in range(groups):
    climbers = int(input())
    if climbers <= 5:
        Musala += climbers
    elif climbers <= 12:
        Montblan += climbers
    elif climbers <= 25:
        Kilimandjaro += climbers
    elif climbers <= 40:
        K2 += climbers
    elif climbers > 40:
        Everest += climbers
    people_total += climbers
p_musala = (Musala / people_total) * 100
p_montblan = (Montblan / people_total) * 100
p_kilimandjaro = (Kilimandjaro / people_total) * 100
p_k2 = (K2 / people_total) * 100
p_everest = (Everest / people_total) * 100
print(f"{p_musala:.2f}%")
print(f"{p_montblan:.2f}%")
print(f"{p_kilimandjaro:.2f}%")
print(f"{p_k2:.2f}%")
print(f"{p_everest:.2f}%")