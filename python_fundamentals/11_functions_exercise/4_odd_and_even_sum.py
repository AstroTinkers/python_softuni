def odd_sum(number):
    list_odd = [i for i in number if i % 2 != 0]
    return sum(list_odd)


def even_sum(number):
    list_even = [i for i in number if i % 2 == 0]
    return sum(list_even)


input_number = [int(i) for i in input()]
print(f"Odd sum = {odd_sum(input_number)}, Even sum = {even_sum(input_number)}")
