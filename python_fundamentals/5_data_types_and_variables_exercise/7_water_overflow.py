fills = int(input())
capacity = 255
full_level = 0
for i in range(0, fills):
    batch = int(input())
    if capacity >= full_level + batch:
        full_level += batch
    else:
        print("Insufficient capacity!")
print(full_level)
