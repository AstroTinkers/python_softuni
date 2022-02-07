def min_num(number):
    return min(number)


def max_num(number):
    return max(number)


def sum_of_nums(number):
    return sum(number)


list_of_numbers = [int(i) for i in input().split(" ")]
print(f"The minimum number is {min_num(list_of_numbers)}")
print(f"The maximum number is {max_num(list_of_numbers)}")
print(f"The sum number is: {sum_of_nums(list_of_numbers)}")
