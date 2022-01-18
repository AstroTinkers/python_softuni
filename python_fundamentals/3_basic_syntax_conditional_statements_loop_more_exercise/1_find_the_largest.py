number = input()
x = [int(a) for a in str(number)]
x.sort(reverse=True)
for i in x:
    print(i, end="")