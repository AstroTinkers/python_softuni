hour = int(input())
day = input()
if 10 > hour or hour > 18 or day == 'Sunday':
    print("closed")
else:
    print("open")