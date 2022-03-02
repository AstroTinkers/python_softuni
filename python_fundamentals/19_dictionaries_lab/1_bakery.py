food_list = input().split(" ")
bakery_dict = {}
for i in range(0, len(food_list), 2):
    bakery_dict[food_list[i]] = int(food_list[i+1])

print(bakery_dict)
