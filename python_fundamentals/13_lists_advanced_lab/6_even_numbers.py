number_list = list(map(int, input().split(", ")))
even_numbers = [idx for (idx, i) in enumerate(number_list) if i % 2 == 0]
print(even_numbers)
