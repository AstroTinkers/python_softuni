from math import ceil
number = int(input())
n_count = 0
for n in range(ceil(number / 2)):
    if n == 0:
        if number % 2 == 0:
            print(f"{(ceil((number / 2) - 1)) * '-'}{2 * '*'}{(ceil((number / 2) - 1)) * '-'}")
            n_count = 2
        else:
            print(f"{(ceil((number / 2) - 1)) * '-'}*{(ceil((number / 2) - 1)) * '-'}")
            n_count = 1
    elif n != 0:
        n_count += 2
        print(f"{ceil((number - (n_count + 1))/2) * '-'}{n_count * '*'}{ceil((number - (n_count + 1))/2) * '-'}")

for n in range(1, number - (int((number + 1)/2)) + 1):
    print(f"|{(number - 2) * '*'}|")
