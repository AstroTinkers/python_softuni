adventure_days = int(input())
party_size = int(input())
energy = float(input())
water = party_size * float(input()) * adventure_days
food = party_size * float(input()) * adventure_days
finished = True
for i in range(1, adventure_days + 1):
    energy -= float(input())
    if energy <= 0:
        finished = False
        break
    if i % 2 == 0:
        energy += energy * .05
        water -= water * .3
    if i % 3 == 0:
        food -= food / party_size
        energy += energy * .1
if finished:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
