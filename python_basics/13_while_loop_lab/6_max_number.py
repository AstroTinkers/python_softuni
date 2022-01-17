import sys
max_num = -sys.maxsize
number = input()
while number != "Stop":
    real_num = int(number)
    if real_num > max_num:
        max_num = real_num
    number = input()
print(max_num)