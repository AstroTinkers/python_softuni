number_list = list(map(int, input().split(", ")))
even_numbers = [idx for (idx, i) in enumerate(number_list) if i % 2 == 0]
# even_numbers = [number_list.index(x) for x in list(filter(lambda x: x % 2 == 0, number_list))]
print(even_numbers)
