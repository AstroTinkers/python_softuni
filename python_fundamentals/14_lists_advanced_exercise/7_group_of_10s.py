number_group = [int(i) for i in input().split(", ")]
modifier = 10
while len(number_group) > 0:
    new_group = [i for i in number_group if i <= modifier]
    print(f"Group of {modifier}'s: {new_group}")
    modifier += 10
    number_group = list(filter(lambda x: x not in new_group, number_group))
