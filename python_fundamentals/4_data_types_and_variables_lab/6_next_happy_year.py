year = int(input())
while True:
    year += 1
    year_set = set(str(year))
    if len(year_set) == len(str(year)):
        break
print(year)