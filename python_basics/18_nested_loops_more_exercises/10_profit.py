_1_lv = int(input())
_2_lv = int(input())
_5_lv = int(input())
total_sum = int(input())

for i in range(_1_lv + 1):
    for j in range(_2_lv + 1):
        for k in range(_5_lv + 1):
            if total_sum == i + j * 2 + k * 5:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {total_sum} lv.")