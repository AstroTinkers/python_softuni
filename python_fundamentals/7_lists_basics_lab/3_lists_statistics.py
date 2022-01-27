num_count = int(input())
positive_num = list()
negative_num = list()
for i in range(num_count):
    number = int(input())
    if number >= 0:
        positive_num.append(number)
    else:
        negative_num.append((number))
print(positive_num)
print(negative_num)
negative_sum = sum(negative_num)
print(f"Count of positives: {len(positive_num)}")
print(f"Sum of negatives: {negative_sum}")
