input_data = input().split(" ")
my_dict = {word.lower(): 0 for word in input_data}
for word in input_data:
    my_dict.setdefault(word.lower(), 0)
    my_dict[word.lower()] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
