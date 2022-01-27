numbers = input()
numbers_list = numbers.split(" ")
numbers_inverted = [(int(num) * -1) for num in numbers_list]
print(numbers_inverted)
