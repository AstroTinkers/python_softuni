gifts = input()
gift_list = gifts.split(" ")
while True:
    shopping = input()
    if shopping == "No Money":
        break
    elif shopping.startswith("OutOfStock"):
        gift = shopping.split()[1]
        for j, m in enumerate(gift_list):
            if m == gift:
                gift_list[j] = None
    elif shopping.startswith("Required"):
        gift_parts = shopping.split()
        gift = gift_parts[1]
        index = int(gift_parts[2])
        if 0 <= index < len(gift_list):
            gift_list[index] = gift
    elif shopping.startswith("JustInCase"):
        gift = shopping.split()
        gift_list[-1] = gift[1]
gifts_list = " ".join([str(i) for i in gift_list if i is not None])
print(gifts_list)
