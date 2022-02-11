names_list = input().split(", ")
names_list = sorted(names_list, key=lambda i: (-len(i), i))
print(names_list)
