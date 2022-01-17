k_start_first_first = int(input())
l_start_second_first = int(input())
m_start_first_second = int(input())
n_start_second_second = int(input())
counter = 0
for k in range(k_start_first_first, 8 + 1):
    if k % 2 != 0:
        continue
    if counter == 6:
        break
    for l in range(9, l_start_second_first - 1, -1):
        if l % 2 == 0:
            continue
        if counter == 6:
            break
        for m in range(m_start_first_second, 8 + 1):
            if m % 2 != 0:
                continue
            if counter == 6:
                break
            for n in range(9, n_start_second_second - 1, -1):
                if n % 2 == 0:
                    continue
                elif k == m and l == n:
                    print("Cannot change the same player.")
                else:
                    print(f"{k}{l} - {m}{n}")
                    counter += 1
                if counter == 6:
                    break
