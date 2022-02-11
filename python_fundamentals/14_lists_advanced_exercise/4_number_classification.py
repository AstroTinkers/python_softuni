def list_conv(given_list):
    return ", ".join([str(i) for i in given_list])


num_list = list(map(int, input().split(", ")))
even_list = [i for i in num_list if abs(i) % 2 == 0]
positive_list = [i for i in num_list if i >= 0]
odd_list = [i for i in num_list if abs(i) % 2 != 0]
negative_list = [i for i in num_list if i < 0]
print(f"Positive: {list_conv(positive_list)}\n"
      f"Negative: {list_conv(negative_list)}\n"
      f"Even: {list_conv(even_list)}\n"
      f"Odd: {list_conv(odd_list)}")
