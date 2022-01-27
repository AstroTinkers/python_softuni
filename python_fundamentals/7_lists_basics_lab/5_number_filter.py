lines = int(input())
numbers = []
filter_list = []
for i in range(lines):
    given_number = int(input())
    numbers.append(given_number)
command = input()
if command == "even":
    filter_list = [num for num in numbers if num % 2 == 0]
elif command == "odd":
    filter_list = [num for num in numbers if num % 2 != 0]
elif command == "negative":
    filter_list = [num for num in numbers if num < 0]
elif command == "positive":
    filter_list = [num for num in numbers if num >= 0]
print(filter_list)
