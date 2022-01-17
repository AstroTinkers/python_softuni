trip_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.6 * puzzles
talking_doll_price = 3 * talking_dolls
teddy_bear_price = 4.1 * teddy_bears
minion_price = 8.2 * minions
truck_price = 2 * trucks

final_sum = puzzle_price + talking_doll_price + teddy_bear_price + minion_price + truck_price

if (puzzles + talking_dolls + teddy_bears + minions + trucks) >= 50:
    final_sum = (puzzle_price + talking_doll_price + teddy_bear_price + minion_price + truck_price) * 0.75

rent = final_sum * 0.1
final_sum -= rent

expences = final_sum - trip_price

if final_sum >= trip_price:
    print(f"Yes! {abs(expences):.2f} lv left.")
else:
    print(f"Not enough money! {abs(expences):.2f} lv needed.")