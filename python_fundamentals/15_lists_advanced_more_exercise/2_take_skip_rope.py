input_list = [i for i in input()]
num_list = [int(i) for i in input_list if i.isnumeric()]
non_num_list = [i for i in input_list if not i.isnumeric()]
take_list = [i for (idx, i) in enumerate(num_list) if idx % 2 == 0]
skip_list = [i for (idx, i) in enumerate(num_list) if idx % 2 != 0]
result = []
for i in take_list:
    result += non_num_list[:i]
    del non_num_list[:i]
    for j in skip_list:
        del non_num_list[:j]
        skip_list.pop(0)
        break
print("".join(result))
