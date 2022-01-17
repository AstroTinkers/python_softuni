import sys
min_num = sys.maxsize
number = input()
while number != "Stop":
    real_num = int(number)
    if real_num < min_num:
        min_num = real_num
    number = input()
print(min_num)