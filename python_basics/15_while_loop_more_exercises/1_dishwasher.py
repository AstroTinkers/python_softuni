detergent_bottles = int(input())
detergent_quantity = detergent_bottles * 750
detergent_over = False
program_over = False
washes = 0
dishes_washed = 0
pots_washed = 0
load = input()
while not(detergent_over and program_over):
    if load == "End":
        program_over = True
        break
    else:
        load = int(load)
    washes += 1
    if washes % 3 == 0:
        pots_washed += load
        detergent_quantity -= load * 15
    else:
        dishes_washed += load
        detergent_quantity -= load * 5
    if detergent_quantity < 0:
        detergent_over = True
        break
    load = input()
if program_over:
    print("Detergent was enough!")
    print(f"{dishes_washed} dishes and {pots_washed} pots were washed.")
    print(f"Leftover detergent {detergent_quantity} ml.")
if detergent_over:
    print(f"Not enough detergent, {abs(detergent_quantity)} ml. more necessary!")