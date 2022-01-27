teams = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11",
         "B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
cards = input()
cards_list = cards.split(" ")
game_finished = True
for i in cards_list:
    if i in teams:
        teams.remove(i)
    if len([i for i in teams if i.startswith('A')]) < 7 or len([i for i in teams if i.startswith('B')]) < 7:
        print(f"Team A - {len([i for i in teams if i.startswith('A')])}; "
              f"Team B - {len([i for i in teams if i.startswith('B')])}")
        print("Game was terminated")
        game_finished = False
        break
if game_finished:
    print(f"Team A - {len([i for i in teams if i.startswith('A')])}; "
          f"Team B - {len([i for i in teams if i.startswith('B')])}")
