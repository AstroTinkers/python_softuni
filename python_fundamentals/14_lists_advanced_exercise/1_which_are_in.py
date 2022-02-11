first_string = input().split(", ")
second_string = input().split(", ")
final_string = [x for x in first_string if any(filter(lambda i: x in i, second_string))]
print(final_string)
