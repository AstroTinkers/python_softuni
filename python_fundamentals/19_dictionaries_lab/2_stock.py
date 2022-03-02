food_list = input().split(" ")
stock = {}
for i in range(0, len(food_list), 2):
    stock[food_list[i]] = int(food_list[i + 1])
requested_items = input().split(" ")
for item in range(0, len(requested_items)):
    if stock.get(requested_items[item]) is not None:
        print(f"We have {stock.get(requested_items[item])} of {requested_items[item]} left")
    else:
        print(f"Sorry, we don't have {requested_items[item]}")
        