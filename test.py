sorted_players = {'Mid': 200, 'Support': 250}

print(sorted_players)
for pos, point in sorted_players.items():
    sorted_players = {pos: point for pos, point in sorted(sorted_players.items(), key=lambda x: (-x[1], x[0]))}

print(sorted_players)