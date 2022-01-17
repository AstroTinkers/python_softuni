import sys
iterations = int(input())
num_max = -sys.maxsize
num_min = sys.maxsize
number = 0
for i in range(iterations):
    number = int(input())
    if number > num_max:
        num_max = number
    if number < num_min:
        num_min = number
print(f"Max number: {num_max}")
print(f"Min number: {num_min}")