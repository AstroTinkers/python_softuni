def rounding(numbers):
    rounded_list = [float(a) for a in numbers.split(" ")]
    rounded_list = [round(a) for a in rounded_list]
    return rounded_list


given_numbers = input()
print(rounding(given_numbers))
