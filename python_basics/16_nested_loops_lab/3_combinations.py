number = int(input())
possible_combinations = 0
for n1 in range(number+1):
    for n2 in range(number+1):
        for n3 in range(number+1):
            if n1 + n2 + n3 == number:
                possible_combinations += 1
print(possible_combinations)
