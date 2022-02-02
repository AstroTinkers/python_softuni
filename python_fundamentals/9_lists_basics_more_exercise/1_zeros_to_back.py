numbers = input().split(", ")
numbers.sort(key="0".__eq__)
numbers = list(map(int, numbers))
print(numbers)
