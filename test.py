list = [2, 4, 6, 8]
list1 = [i for i in list if i % 2 != 0]
print(min(list1, default=None))
