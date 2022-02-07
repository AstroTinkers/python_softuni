def even_nums(number):
    return number % 2 == 0


input_numbers = [int(i) for i in input().split(" ")]
even_numbers = filter(even_nums, input_numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)
