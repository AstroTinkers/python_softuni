start_first_pair = int(input())
start_second_pair = int(input())
difference_first_pair = int(input())
difference_second_pair = int(input())

for i in range(start_first_pair, start_first_pair + difference_first_pair + 1):
    for j in range(start_second_pair, start_second_pair + difference_second_pair + 1):

        i_is_prime = True
        j_is_prime = True

        for k in range(2, i):
            if i % k == 0:
                i_is_prime = False
                break

        for m in range(2, j):
            if j % m == 0:
                j_is_prime = False
                break
        if i_is_prime and j_is_prime:
            print(f"{i}{j}")
