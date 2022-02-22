int_list = [int(input()), int(input()), int(input())]
pos_list = [i for i in int_list if i > 0]
neg_list = [i for i in int_list if i < 0]
if 0 in int_list:
    print("zero")
elif len(neg_list) % 2 == 0:
    print("positive")
else:
    print("negative")
